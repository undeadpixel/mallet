import random
import safe_math


class State(object):

    def __init__(self, id_num, long_name, short_name, emissions = None, transitions = None):
        """
        Initializes a State:
            + long_name: A descriptive name
            + short_name: A one letter name
            + emissions: A hash with all the possible emissions and the associated probability.
            + transitions: A hash comprised by pairs of (State -> probability). Usually is set later on using state.transitions = {...}
        """
        if emissions is None: emissions = {}
        if transitions is None: transitions = {}

        self.id_num = id_num
        self.long_name = long_name
        self.short_name = short_name
        self.emissions = emissions
        self.transitions = transitions

        # some internal attributes
        self.__log_transitions_cache = None
        self.__log_emissions_cache = None
        self.__transition_items_cache = None
        self.__emission_items_cache = None

    def is_valid(self):
        """
        Checks if the HMM is valid and raises an error if not:
            + Checks if emissions sum up 1.
            + Checks short name has only one letter.
        """
        if not self.is_begin() and not self.is_end():
            self.__check_short_name()
            self.__check_emissions_probability_sum()

        if not self.is_end():
            self.__check_transitions_probability_sum()

        return True

    def is_begin(self):
        """
        Returns true when state is BEGIN.
        """
        return self.short_name == "BEGIN"

    def is_end(self):
        """
        Returns true when state is END.
        """
        return self.short_name == "END"

    def sample_transition(self):
        """
        Returns a random state for the given transitions using the same probability distribution. Of course, transitions should sum probability 1...
        """
        return self.__sample_from_discrete_values(self.__transition_items())

    def sample_emission(self):
        """
        Returns a sample emission from this state using the emissions probability distribution.
        """
        return self.__sample_from_discrete_values(self.__emission_items())

    def log_transitions(self):
        """
        Returns a dict with transition probabilities converted to log10.
        """
        if self.__log_transitions_cache is None:
            self.__log_transitions_cache = self.__log_distribution(self.transitions)
        return self.__log_transitions_cache

    def log_emissions(self):
        """
        Returns a dict with emission probabilities converted to log10.
        """
        if self.__log_emissions_cache is None:
            self.__log_emissions_cache = self.__log_distribution(self.emissions)
        return self.__log_emissions_cache

    # for comparing and printing
    def simple_transitions(self):
        return dict((state.short_name, prob) for state,prob in self.transitions.iteritems())

    # equality operator
    def __eq__(self, other_state):
        return(self.id_num == other_state.id_num and self.long_name == other_state.long_name
                and self.short_name == other_state.short_name and self.emissions == other_state.emissions
                and self.simple_transitions() == other_state.simple_transitions())

    # string legible representation
    def __repr__(self):
        output = "[ State: {} - {} - {} | ".format(self.long_name, self.short_name, self.id_num)
        output += "Emissions: {} | ".format(self.emissions)
        output += "Transitions: {}]".format(self.simple_transitions())
        return output

    # methods for getting and setting transitions
    def get_transition_state(self, state_id):
        return next(state for state,prob in self.transitions.iteritems() if state.id_num == state_id)

    def set_transition_state(self, state_id, probability):
        self.transitions[self.get_transition_state(state_id)] = probability
    # private

    def __check_emissions_probability_sum(self):
        probability_sum = sum([probability for (name,probability) in self.emissions.iteritems()], 0.0)
        if round(probability_sum, 4) != 1.0:
            raise ValueError("State {} has invalid emissions: they sum {:.4f}. It should be 1.0.".format(self.long_name, probability_sum))

    def __check_short_name(self):
        if len(self.short_name) != 1:
            raise ValueError("State {} has an invalid short name '{}': it should be one letter".format(self.long_name, self.short_name))

    def __check_transitions_probability_sum(self):
        probability_sum = sum([probability for (state,probability) in self.transitions.iteritems()], 0.0)
        if round(probability_sum, 4) != 1.00:
            raise ValueError("State {} has invalid transitions: they sum {:.4f}. It should be 1.0.".format(self.long_name, probability_sum))

    def __log_distribution(self, distribution):
        log_distribution = {}
        for state,prob in distribution.iteritems():
            log_distribution[state] = safe_math.log10(prob)
        return log_distribution

    # NOTE: This is used to force order on transitions and emissions. If not used, we have that the dict order may change on different executions, thus giving different samples for the same probabilities.
    def __transition_items(self):
        if self.__transition_items_cache is None:
            self.__transition_items_cache = sorted(self.transitions.items(), key=lambda i: i[0].short_name)
        return self.__transition_items_cache

    def __emission_items(self):
        if self.__emission_items_cache is None:
            self.__emission_items_cache = sorted(self.emissions.items())
        return self.__emission_items_cache

    def __sample_from_discrete_values(self, distribution):
        random_probability = random.random()
        accumulated_probability = 0.0
        for value,prob in distribution:
            accumulated_probability += prob
            if accumulated_probability > random_probability:
                return value

