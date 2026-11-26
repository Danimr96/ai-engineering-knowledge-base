import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bpe import BPETokenizer, fertility, get_pairs, merge_pair, wordpiece_score

class TestPrimitives(unittest.TestCase):
    def test_get_pairs_counts_adjacent(self):
        self.assertEqual(get_pairs([1,2,1,2,3]), {(1,2):2,(2,1):1,(2,3):1})
    def test_get_pairs_empty_and_single(self):
        self.assertEqual(dict(get_pairs([])), {}); self.assertEqual(dict(get_pairs([7])), {})
    def test_merge_pair_replaces_all_non_overlapping(self):
        self.assertEqual(merge_pair([1,2,1,2,2,1], (1,2), 9), [9,9,2,1])
    def test_merge_pair_left_to_right_on_overlap(self):
        # "aaa" with pair (a,a): first two merge, third stays
        self.assertEqual(merge_pair([1,1,1], (1,1), 9), [9,1])

class TestTraining(unittest.TestCase):
    def test_base_vocab_is_256_bytes(self):
        t=BPETokenizer(); self.assertEqual(len(t.vocab),256); self.assertEqual(t.vocab[104], b"h")
    def test_first_merge_is_most_frequent_pair(self):
        t=BPETokenizer().train("aaab aaab aaab", 1)
        self.assertEqual(list(t.merges.keys())[0], (97,97)); self.assertEqual(t.vocab[256], b"aa")
    def test_merges_build_on_earlier_merges(self):
        t=BPETokenizer().train("the the the the", 3)
        self.assertIn(b"the", t.vocab.values())
    def test_stops_when_no_pair_repeats(self):
        t=BPETokenizer().train("abcdef", 50)
        self.assertEqual(len(t.merges), 0)
    def test_vocab_grows_by_num_merges(self):
        t=BPETokenizer().train("hipoteca hipotecario hipotecas hipoteca hipotecario", 10)
        self.assertEqual(len(t.vocab), 256+len(t.merges)); self.assertLessEqual(len(t.merges),10)

class TestEncodeDecode(unittest.TestCase):
    CORPUS="el cliente solicitó una hipoteca. el cliente pagó la hipoteca. la hipoteca del cliente."
    def test_roundtrip_in_distribution(self):
        t=BPETokenizer().train(self.CORPUS, 30)
        s="el cliente pagó la hipoteca."; self.assertEqual(t.decode(t.encode(s)), s)
    def test_roundtrip_unicode_out_of_distribution(self):
        t=BPETokenizer().train(self.CORPUS, 30)
        s="客户申请了抵押贷款 — ñandú 🦙"; self.assertEqual(t.decode(t.encode(s)), s)
    def test_encode_compresses_training_text(self):
        t=BPETokenizer().train(self.CORPUS, 30)
        s="la hipoteca del cliente."; self.assertLess(len(t.encode(s)), len(s.encode("utf-8")))
    def test_encode_applies_merges_in_learned_order(self):
        t=BPETokenizer().train("the the the the", 3)
        ids=t.encode("the"); self.assertEqual(len(ids),1); self.assertEqual(t.vocab[ids[0]], b"the")
    def test_unseen_text_falls_back_to_bytes(self):
        t=BPETokenizer().train("aaaa aaaa", 2)
        self.assertEqual(t.encode("xyz"), [120,121,122])

class TestMetrics(unittest.TestCase):
    def test_wordpiece_prefers_surprising_pairs(self):
        # (A,B) seen 10 times, A and B each 10 times -> always together
        # (C,D) seen 10 times, C and D each 1000 times -> chance
        self.assertGreater(wordpiece_score(10,10,10), wordpiece_score(10,1000,1000))
    def test_fertility_is_tokens_per_word(self):
        t=BPETokenizer()  # no merges: 1 token per byte
        self.assertAlmostEqual(fertility(t,"ab cd ef"), 8/3)  # 8 bytes (spaces count!) / 3 words
        self.assertEqual(fertility(t,""), 0.0)

if __name__=="__main__": unittest.main()
