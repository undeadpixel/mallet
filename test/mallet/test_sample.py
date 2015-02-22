import test.helpers as helpers
import nose.tools as nt
import mock

import mallet.sample as sample
import mallet.alignment as alignment
import mallet.sequence as seq
import mallet.input.tgf_parser as tgf

# import some fixtures
import test.fixtures.hmm_fixtures as fixtures

def new_alignment(sequence, state_path, score = None):
    return alignment.Alignment(seq.Sequence("Sequence", sequence), seq.Sequence("State path", state_path), score)

class TestSample(object):

    def subject(self, hmm = None, observations = 10):
        if hmm is None: hmm = tgf.parse("test/files/tgf/simple.tgf")
        return sample.sample(hmm, observations)

    def test_zero_observations(self):
        alignment = self.subject(observations = 0)
        nt.assert_equals(alignment, new_alignment("", ""))

    @mock.patch('random.random', side_effect=[0.9, 0.1, 0.6, 0.65, 0.8, 0.9])
    def test_min_observations(self, random_mock):
        alignment = self.subject(observations = 3)
        nt.assert_equals(alignment, new_alignment("ABC", "STU"))

    @mock.patch('random.random', return_value = 0.3)
    def test_not_ending_observations(self, random_mock):
        alignment = self.subject(observations = 5)
        nt.assert_equals(alignment, new_alignment("BBBBB", "SSSSS"))

    @mock.patch('random.random', side_effect=[0.9, 0.1, 0.6, 0.65, 0.8, 0.9, 0.1])
    def test_ending_early_observations(self, random_mock):
        alignment = self.subject(observations = 300)
        nt.assert_equals(alignment, new_alignment("ABC", "STU"))
