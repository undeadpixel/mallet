import test.mallet.helpers as helpers
import nose.tools as nt

import mallet.state as state

# import some fixtures
import test.fixtures.hmm_fixtures as fixtures

class TestState(object):

    def subject(self, num_id = 1, long_name = "Test state", short_name = "S", emissions = fixtures.emissions()[0], transitions = fixtures.transitions()[2]):
        return state.State(num_id, long_name, short_name, emissions, transitions)

    def test_is_valid_state(self):
        assert(self.subject().is_valid())

    def test_is_invalid_state_short_name(self):
        nt.assert_raises(ValueError, self.subject(short_name = "S1").is_valid)

    def test_is_invalid_state_emissions(self):
        nt.assert_raises(ValueError, self.subject(emissions = fixtures.invalid_emissions()[0]).is_valid)

    def test_is_invalid_state_empty_transitions(self):
        nt.assert_raises(ValueError, self.subject(transitions = {}).is_valid)

    def test_is_valid_state_transitions(self):
        assert(self.subject().is_valid())
