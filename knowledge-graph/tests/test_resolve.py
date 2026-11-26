"""kg.extract.resolve: normalisation and the three matching tiers."""

from kg.extract.resolve import ConceptIndex, normalize, singular, split_parenthetical, variants


def test_normalize_folds_spelling_variants():
    assert normalize("KV cache") == normalize("KV-Cache") == normalize("kv_cache") == "kv-cache"
    assert normalize("**Grouped-Query Attention (GQA)**") == "grouped-query-attention-gqa"
    assert normalize("Math & training") == "math-and-training"
    assert normalize("`P(a | b)`") == "p-a-b"


def test_parenthetical_and_singular():
    assert split_parenthetical("Automatic Speech Recognition (ASR)") == ("Automatic Speech Recognition", "ASR")
    assert split_parenthetical("Attention") == ("Attention", None)
    assert singular("embeddings") == "embedding"
    assert singular("policies") == "policy"
    assert singular("bias") is None
    assert singular("loss") is None


def test_variants_order():
    v = variants("Grouped-Query Attention (GQA)")
    assert v[0] == ("grouped-query-attention-gqa", "exact")
    assert ("grouped-query-attention", "normalized") in v
    assert ("gqa", "alias") in v


def test_index_match_tiers():
    idx = ConceptIndex()
    idx.add_canonical("concept:kv-cache", "KV Cache", aliases=["key-value cache"])
    idx.add_canonical("concept:automatic-speech-recognition-asr", "Automatic Speech Recognition (ASR)")
    idx.add_canonical("concept:embedding", "Embedding")

    assert idx.match("KV cache") == ("concept:kv-cache", "exact")
    assert idx.match("key-value cache") == ("concept:kv-cache", "alias")
    assert idx.match("ASR") == ("concept:automatic-speech-recognition-asr", "alias")
    # the heading without its "(ASR)" is registered as an alias of the heading
    assert idx.match("Automatic Speech Recognition") == ("concept:automatic-speech-recognition-asr", "alias")
    assert idx.match("Embeddings") == ("concept:embedding", "normalized")
    assert idx.match("Flash attention") is None


def test_manual_aliases():
    idx = ConceptIndex()
    idx.add_canonical("concept:few-shot", "Few-Shot")
    problems = idx.add_manual_aliases({"_comment": "x", "few-shot prompting": "Few-Shot", "typo": "Nope"})
    assert idx.match("Few-shot PROMPTING") == ("concept:few-shot", "alias")
    assert problems == ["aliases.json: 'typo' -> unknown glossary term 'Nope'"]
