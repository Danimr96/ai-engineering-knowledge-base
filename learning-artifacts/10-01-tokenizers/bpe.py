"""Phase 10 · Lesson 01 · Tokenizers — byte-level BPE, the GPT-2 way.

Run the tests:
    cd "learning-artifacts/10-01-tokenizers"
    ../../ai-engineering-from-scratch/.venv/bin/python -m unittest discover tests -v

Run the demo (trains on a Spanish banking corpus, shows merges, compares with tiktoken):
    ../../ai-engineering-from-scratch/.venv/bin/python bpe.py

Only the standard library is used. Read the comments: they explain the *why*.
"""
from collections import Counter


# --------------------------------------------------------------------------
# Two primitives. The whole algorithm is built from these.
# --------------------------------------------------------------------------

def get_pairs(tokens: list[int]) -> Counter:
    """Count every adjacent pair in `tokens`.

    [1, 2, 1, 2, 3] -> {(1,2): 2, (2,1): 1, (2,3): 1}

    zip(tokens, tokens[1:]) walks the list two at a time: (t0,t1), (t1,t2), ...
    Counter keeps insertion order, which is what makes the tie-break in train()
    deterministic ("first pair seen in the stream wins").
    """
    return Counter(zip(tokens, tokens[1:]))


def merge_pair(tokens: list[int], pair: tuple[int, int], new_id: int) -> list[int]:
    """Replace every non-overlapping occurrence of `pair` with `new_id`, left to right.

    [1,1,1] with pair (1,1) -> [9, 1]: the first two merge, the third has no partner.

    One pass, one index. When we hit a match we emit new_id and jump by 2,
    so the second element of a match can never start another match.
    """
    out = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and tokens[i] == pair[0] and tokens[i + 1] == pair[1]:
            out.append(new_id)
            i += 2
        else:
            out.append(tokens[i])
            i += 1
    return out


# --------------------------------------------------------------------------
# The tokenizer. Train = learn merges. Encode = replay merges. Decode = look up bytes.
# --------------------------------------------------------------------------

class BPETokenizer:
    """Byte-level BPE.

    - Base vocabulary: the 256 possible bytes, ids 0..255, vocab[i] == bytes([i]).
      Any text in any script is a sequence of bytes, so nothing is ever "unknown".
    - Each merge k (starting at 0) creates id 256 + k.
    - self.merges: (left_id, right_id) -> new_id, in the ORDER they were learned.
      Python dicts keep insertion order; encode() depends on that.
    - self.vocab: id -> bytes. This is what decode() reads.
    """

    def __init__(self):
        self.merges: dict[tuple[int, int], int] = {}
        self.vocab: dict[int, bytes] = {i: bytes([i]) for i in range(256)}

    def train(self, text: str, num_merges: int) -> "BPETokenizer":
        """Learn up to `num_merges` merges from `text`.

        Loop: count pairs -> pick the most frequent -> merge it everywhere -> record it.
        Stop early if no pair occurs at least twice: a merge for a pair seen once
        creates a token that will never be reused, which is wasted vocabulary.
        """
        tokens = list(text.encode("utf-8"))          # str -> list of ints 0..255
        for k in range(num_merges):
            pairs = get_pairs(tokens)
            if not pairs:
                break
            best = max(pairs, key=pairs.get)         # first max in stream order on ties
            if pairs[best] < 2:
                break
            new_id = 256 + k
            tokens = merge_pair(tokens, best, new_id)
            self.merges[best] = new_id
            self.vocab[new_id] = self.vocab[best[0]] + self.vocab[best[1]]
        return self

    def encode(self, text: str) -> list[int]:
        """Bytes in, ids out. Replay the learned merges in the order they were learned.

        Why the order matters: merge 7 might be (th, e). The token "th" only exists
        after merge 2. Replay them out of order and "the" can never form.
        """
        tokens = list(text.encode("utf-8"))
        for pair, new_id in self.merges.items():
            tokens = merge_pair(tokens, pair, new_id)
        return tokens

    def decode(self, ids: list[int]) -> str:
        """Ids in, text out. Concatenate the bytes, then decode as UTF-8.

        errors="replace" because a single id can be half of a multi-byte character
        (e.g. one byte of "ñ"); if you decode a truncated stream you get "�" instead of a crash.
        """
        return b"".join(self.vocab[i] for i in ids).decode("utf-8", errors="replace")


# --------------------------------------------------------------------------
# Two metrics from the lesson.
# --------------------------------------------------------------------------

def wordpiece_score(pair_count: int, left_count: int, right_count: int) -> float:
    """WordPiece's merge criterion: co-occurrence relative to chance.

    BPE ranks pairs by pair_count alone. WordPiece divides by count(A) * count(B),
    so a pair of two very common symbols ("e", " ") scores low: seeing them together
    is expected, not informative. A rarer pair that almost always co-occurs scores high.
    """
    return pair_count / (left_count * right_count)


def fertility(tokenizer: BPETokenizer, text: str) -> float:
    """Average tokens per whitespace-separated word. 0.0 for empty text.

    Spaces are bytes too, so they count as tokens: that is how real tokenizers see text.
    1.0 would mean one token per word; GPT-2 on Korean is closer to 10.
    """
    words = text.split()
    if not words:
        return 0.0
    return len(tokenizer.encode(text)) / len(words)


# --------------------------------------------------------------------------
# Demo
# --------------------------------------------------------------------------

def _show(tok: BPETokenizer, ids: list[int]) -> str:
    return " | ".join(tok.vocab[i].decode("utf-8", errors="replace").replace(" ", "␣") for i in ids)


if __name__ == "__main__":
    corpus = (
        "el cliente solicitó una hipoteca. el cliente pagó la hipoteca. "
        "la hipoteca del cliente tiene un tipo de interés fijo. "
        "el préstamo hipotecario del cliente se firmó en la sucursal. "
        "la cuenta del cliente y la cuenta de la empresa tienen saldo. "
        "el cliente pidió un extracto de la cuenta y de la hipoteca."
    )
    tok = BPETokenizer().train(corpus, num_merges=60)

    print("=" * 66)
    print("  MERGES LEARNED (in order)")
    print("=" * 66)
    for k, ((a, b), new_id) in enumerate(tok.merges.items()):
        left, right, merged = (tok.vocab[x].decode("utf-8", "replace").replace(" ", "␣") for x in (a, b, new_id))
        print(f"  {k:2d}: {left!r:>8} + {right!r:<8} -> id {new_id}  {merged!r}")

    print()
    print("=" * 66)
    print("  ENCODE / DECODE")
    print("=" * 66)
    for s in ["la hipoteca del cliente.", "hipotecarias", "préstamo", "customer account", "客户申请 🦙"]:
        ids = tok.encode(s)
        ok = tok.decode(ids) == s
        print(f"  {s!r}")
        print(f"     {len(s.encode('utf-8')):3d} bytes -> {len(ids):3d} tokens   roundtrip {'OK' if ok else 'FAIL'}")
        print(f"     {_show(tok, ids)}")

    print()
    print("=" * 66)
    print("  FERTILITY (tokens per word) — ours vs tiktoken cl100k")
    print("=" * 66)
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")

        class _TT:  # tiny adapter so fertility() can take tiktoken too
            def encode(self, s): return enc.encode(s)
        tt = _TT()
    except ImportError:
        tt = None
    for s in [
        "el cliente pidió un extracto de la cuenta",           # in-distribution
        "la sucursal aprobó la refinanciación del préstamo",   # Spanish, unseen words
        "the customer requested an account statement",         # English
    ]:
        ours = fertility(tok, s)
        line = f"  {ours:5.2f}  ours(60 merges, 1 paragraph)"
        if tt:
            line += f"   {fertility(tt, s):5.2f}  cl100k(100k merges, ~TBs)"
        print(f"  {s!r}\n{line}")

    print()
    print("=" * 66)
    print("  BPE vs WORDPIECE on two candidate pairs")
    print("=" * 66)
    for name, pc, a, b in [("('hipo','teca')", 40, 45, 50), ("('e',' ')", 120, 1500, 1800)]:
        print(f"  {name:<18} BPE score {pc:4d}   WordPiece score {wordpiece_score(pc, a, b):.2e}")
    print("  BPE picks the second (bigger count); WordPiece picks the first (more surprising).")
