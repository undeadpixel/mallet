
class HMM(object):
    
    def __init__(self, states):
        """
        Initializes a HMM:
            - states: A hash comprised by all states completely loaded and valid.
        """
        self.states = states

    def is_valid(self):
        """
        Checks if the HMM is valid and raises an error if not:
            + Checks that states are valid.
            + Checks that there are no states with equal name or short name
        """
        self.__check_states()
        self.__check_state_names()
        self.__check_has_begin_state()
        self.__check_has_end_state()

        return True

    def begin_state(self):
        """
        Returns the begin state if the model has it.
        """
        return next((state for id_num,state in self.states.iteritems() if state.is_begin()), None)

    # equality operator
    def __eq__(self, other_hmm):
        return self.states == other_hmm.states

    # private

    def __check_states(self):
        for (short_name, state) in self.states.iteritems():
            state.is_valid()

    def __check_state_names(self):
        short_names = [state.short_name for (short_name, state) in self.states.iteritems()]
        long_names = [state.long_name for (long_name, state) in self.states.iteritems()]

        if len(set(short_names)) != len(short_names):
            raise ValueError("HMM has repeated short state names.")
        elif len(set(long_names)) != len(long_names):
            raise ValueError("HMM has repeated long state names.")

    def __check_has_begin_state(self):
        if not any(state.is_begin() for name, state in self.states.iteritems()):
            raise ValueError("HMM has no begin state")

    def __check_has_end_state(self):
        if not any(state.is_end() for name, state in self.states.iteritems()):
            raise ValueError("HMM has no end state")
