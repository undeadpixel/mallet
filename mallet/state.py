import random
import math

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

    def is_valid(self):
        """
        Checks if the HMM is valid and raises an error if not:
            + Checks if emissions sum up 1.
            + Checks short name has only one letter.
        """
        # TODO: Why don't we create a class hierarchy?
        if not self.is_begin() and not self.is_end():
            self.__check_short_name()
            self.__check_emissions_probability_sum()

        if not self.is_end():
            self.__check_transitions_probability_sum()

        return True

    def is_begin(self):
        return self.short_name == "BEGIN"

    def is_end(self):
        return self.short_name == "END"

    def sample_transition(self):
        """
        Returns a random state for the given transitions using the same probability distribution. Of course, transitions should sum probability 1...
        """
        return self.__sample_from_discrete_values(self.transitions)

    def sample_emission(self):
        """
        Returns a sample emission from this state using the emissions probability distribution.
        """
        return self.__sample_from_discrete_values(self.emissions)

    # TODO: Generify this a little
    def log_transitions(self):
        if not hasattr(self, '__log_transitions') or self.__log_transitions is None:
            self.__log_transitions = {}
            for state,prob in self.transitions.iteritems():
                self.__log_transitions[state] = math.log10(prob)
        return self.__log_transitions

    def log_emissions(self):
        if not hasattr(self, '__log_emissions') or self.__log_emissions is None:
            self.__log_emissions = {}
            for emission,prob in self.emissions.iteritems():
                self.__log_emissions[emission] = math.log10(prob)
        return self.__log_emissions

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

    # private

    def __check_emissions_probability_sum(self):
        probability_sum = sum([probability for (name,probability) in self.emissions.iteritems()], 0.0)
        if probability_sum != 1.0:
            raise ValueError("State {} has invalid emissions: they sum {:.4f}. It should be 1.0.".format(self.long_name, probability_sum))

    def __check_short_name(self):
        if len(self.short_name) != 1:
            raise ValueError("State {} has an invalid short name '{}': it should be one letter".format(self.long_name, self.short_name))

    def __check_transitions_probability_sum(self):
        probability_sum = sum([probability for (state,probability) in self.transitions.iteritems()], 0.0)
        if probability_sum != 1.0:
            raise ValueError("State {} has invalid transitions: they sum {:.4f}. It should be 1.0.".format(self.long_name, probability_sum))

    def __sample_from_discrete_values(self, distribution):
        random_probability = random.random()
        accumulated_probability = 0.0
        for value,prob in distribution.iteritems():
            accumulated_probability += prob
            if accumulated_probability > random_probability:
                return value

