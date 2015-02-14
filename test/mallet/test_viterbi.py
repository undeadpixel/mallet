import test.helpers as helpers
import nose.tools as nt

import mallet.input.tgf_parser as tgf
import mallet.sequence as seq

import mallet.viterbi as viterbi

class TestViterbi(object):

    def subject(self, hmm_filename, sequence):
        return viterbi.viterbi(tgf.parse("test/files/{}".format(hmm_filename)), sequence)

    def assert_alignment(self, alignment, state_path, score):
        nt.assert_equals(alignment.state_path, seq.Sequence("State path", state_path))
        nt.assert_almost_equal(alignment.score, score, 2)

    # sample 1

    def test_sample_1_sequence_1(self):
        alignment = self.subject("sample1.tgf", seq.Sequence("S1", "ABAABB"))
        self.assert_alignment(alignment, "TTTTTT", -3.48)

    def test_sample_1_sequence_2(self):
        alignment = self.subject("sample1.tgf", seq.Sequence("S1", "ABBBBBA"))
        self.assert_alignment(alignment, "TTTTTTT", -3.17)

    def test_sample_1_sequence_3(self):
        alignment = self.subject("sample1.tgf", seq.Sequence("S1", "AAAAAAA"))
        self.assert_alignment(alignment, "SSSSSSU", -5.45)

    # rna_hairpin

    def test_rna_hairpin_sequence_1(self):
        alignment = self.subject("rna_hairpin.tgf", seq.Sequence("S1", "UACGCAUGCAU"))
        self.assert_alignment(alignment, "NNTTTHHTTNN", -8.52)

    def test_rna_hairpin_sequence_2(self):
        alignment = self.subject("rna_hairpin.tgf", seq.Sequence("S1", "AUCAUGAC"))
        self.assert_alignment(alignment, "NNNNNNNN", -7.32)

    def test_rna_hairpin_sequence_3(self):
        alignment = self.subject("rna_hairpin.tgf", seq.Sequence("S1", "CGCCAUAUCG"))
        self.assert_alignment(alignment, "NTTTNNNNNN", -9.99)
