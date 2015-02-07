import test.helpers as helpers
import nose.tools as nt

import mallet.hmm as hmm

# import some fixtures
import test.fixtures.hmm_fixtures as fixtures

class TestHMM(object):

    def subject(self, states = None):
        if not states:
            states = fixtures.states_with_transitions()
        return hmm.HMM(states)

    def test_is_valid_hmm(self):
        assert(self.subject().is_valid())

    def test_is_invalid_hmm_states(self):
        subject = self.subject()
        subject.states[2].emissions = fixtures.invalid_emissions()[0]
        nt.assert_raises(ValueError, subject.is_valid)

    def test_is_invalid_hmm_state_short_name(self):
        subject = self.subject()
        subject.states[2].short_name = 'T'

        nt.assert_raises(ValueError, subject.is_valid)

    def test_is_invalid_hmm_state_long_name(self):
        subject = self.subject()
        subject.states[2].long_name = subject.states[3].long_name

        nt.assert_raises(ValueError, subject.is_valid)

    def test_is_invalid_because_there_is_no_begin_state(self):
        subject = self.subject()
        del(subject.states[1])
        nt.assert_raises(ValueError, subject.is_valid)

    def test_is_invalid_because_there_is_no_end_state(self):
        subject = self.subject()
        del(subject.states[5])
        nt.assert_raises(ValueError, subject.is_valid)

    def test_begin_state(self):
        nt.assert_equals(self.subject().begin_state(), fixtures.states_with_transitions()[1])

    def test_begin_state_without_begin_state(self):
        subject = self.subject()
        del(subject.states[1])
        nt.assert_equals(subject.begin_state(), None)
