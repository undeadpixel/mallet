import test.helpers as helpers
import nose.tools as nt
import mock

import mallet.state as state

# import some fixtures
import test.fixtures.hmm_fixtures as fixtures

class TestState(object):

    def subject(self, num_id = 1, long_name = "Test state", short_name = "S", emissions = None, transitions = None):
        if emissions is None: emissions = fixtures.emissions()[0]
        if transitions is None: transitions = fixtures.transitions()[2]
        return state.State(num_id, long_name, short_name, emissions, transitions)

    # VALIDITY

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

    # SAMPLE

    @mock.patch('random.random', return_value = 0.2)
    def test_sample_emission(self, random_mock):
        nt.assert_equals(self.subject().sample_emission(), "A")

    @mock.patch('random.random', return_value = 0.8)
    def test_sample_emission_with_higher_random_value(self, random_mock):
        nt.assert_equals(self.subject().sample_emission(), "C")

    @mock.patch('random.random', return_value = 0.2)
    def test_sample_transition(self, random_mock):
        nt.assert_equals(self.subject().sample_transition(), fixtures.states()[2])

    @mock.patch('random.random', return_value = 0.9)
    def test_sample_transition_with_higher_random_value(self, random_mock):
        nt.assert_equals(self.subject().sample_transition(), fixtures.states()[3])

    # LOG DISTRIBUTIONS

    def test_log_transitions(self):
        states = fixtures.states()
        transitions = fixtures.transitions(states)[2]
        log_transitions = self.subject(transitions = transitions).log_transitions()
        nt.assert_almost_equal(log_transitions[states[2]], -0.3, 2)
        nt.assert_almost_equal(log_transitions[states[3]], -0.3, 2)

    def test_log_transitions_with_zero_transitions(self):
        states = fixtures.states()
        transitions = fixtures.fake_transitions(states)[1]
        log_transitions = self.subject(transitions = transitions).log_transitions()
        nt.assert_almost_equal(log_transitions[states[2]], 0.0, 2)
        nt.assert_almost_equal(log_transitions[states[3]], -1e50, 2)

    def test_log_emissions(self):
        subject = self.subject()
        log_emissions = subject.log_emissions()
        nt.assert_almost_equal(log_emissions['A'], -0.6, 2)
        nt.assert_almost_equal(log_emissions['B'], -0.6, 2)
        nt.assert_almost_equal(log_emissions['C'], -0.3, 2)

    def test_log_emissions_with_zero_emissions(self):
        subject = self.subject(emissions = fixtures.emissions()[4])
        log_emissions = subject.log_emissions()
        nt.assert_almost_equal(log_emissions['A'], -1e50, 2)
        nt.assert_almost_equal(log_emissions['B'], -0.3, 2)
        nt.assert_almost_equal(log_emissions['C'], -0.3, 2)




