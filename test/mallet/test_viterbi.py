import test.helpers as helpers
import nose.tools as nt

import mallet.viterbi as viterbi

# import some fixtures
import test.fixtures.hmm_fixtures as fixtures
import test.fixtures.sequence_fixtures as seq_fixtures

class TestViterbiMatrix(object):

    def subject(self, states = None, sequence_length = len(seq_fixtures.sequences()[0])):
        if states is None: states = fixtures.states().values()
        return viterbi.ViterbiMatrix(states, sequence_length)

    def test_get_and_set(self):
        states = fixtures.states().values()
        subject = self.subject(states)
        subject.set(states[1], 1, 123.45)
        nt.assert_equals(subject.get(states[1], 1), 123.45)

    def test_connect_and_get_parent(self):
        states = fixtures.states().values()
        subject = self.subject(states)
        subject.connect((states[1], 1), (states[2], 2))
        nt.assert_equals(subject.get_parent(states[1], 1), (states[2], 2))


