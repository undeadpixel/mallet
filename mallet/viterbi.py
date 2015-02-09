import pdb
import sequence as seq

INFINITY = float('inf')

class ViterbiMatrix(object):

    def __init__(self, states, sequence_length):
        self.states = states
        self.sequence_length = sequence_length

        self.__initialize_matrix()

    def get(self, state, i):
        return self.__get(state, i).value

    def set(self, state, i, value):
        self.__get(state, i).value = value

    def connect(self, child_cell, parent_cell = None):
        if parent_cell: parent_cell = self.__get(*parent_cell)
        self.__get(*child_cell).parent = parent_cell

    def get_parent(self, state, i):
        parent = self.__get(state, i).parent
        if parent:
            return (parent.state, parent.position)

    def __repr__(self):
        output = "\t".join(["State"] + [str(i) for i in range(self.sequence_length)]) + "\n"
        for state, array in self.matrix.iteritems():
            output += "{}\t".format(state.short_name) + "\t".join([str(item) for item in array]) + "\n"
        return output

    # private

    def __get(self, state, i):
        return self.matrix[state][i]

    def __initialize_matrix(self):
        def create_row(state):
            return [ViterbiMatrixCell(state, i) for i in range(self.sequence_length)]

        self.matrix = dict((state, create_row(state)) for state in self.states)

class ViterbiMatrixCell(object):

    def __init__(self, state, position):
        self.value = -INFINITY
        self.parent = None
        self.state = state
        self.position = position

    def __repr__(self):
        return "{:.2f}".format(self.value)

# methods

def viterbi_all(hmm, sequences):
    """
    Runs the viterbi algorithm on a list of sequences given a Hidden Markov Model.
    """
    results = []
    for sequence in sequences:
        results.append(viterbi(hmm, sequence))
    return results

def viterbi(hmm, sequence):
    """
    Given a sequence and a HMM, returns the maximal state path.
    """
    states = hmm.states.values()
    # initialize matrix adding two positions for begin and end states
    matrix_sequence = "-{}-".format(sequence.sequence)
    matrix = ViterbiMatrix(states, len(matrix_sequence))

    # set 0 to begin - 0 (and filling up first row)
    matrix.set(hmm.begin_state(), 0, 0.0)

    # we only run through the sequence taking into account that we have done the first row (1...N)
    num_iterations = len(matrix_sequence)
    for position in range(1,num_iterations):
        # we get the current char of the sequence (knowing that we have one position more in the matrix before)
        current_char = matrix_sequence[position]

        # we save all probabilities for all states in a hash to then get the max for each state
        state_values = dict((state, []) for state in states)
        for state in states:
            # as we don't have the anterior transitions but the posterior for each state, we have to do it the opposite way
            for dst_state,transition_probability in state.log_transitions().iteritems():
                # TODO: move to State class!!!
                if dst_state.is_end():
                    emission_value = 0.0
                else:
                    emission_value = dst_state.log_emissions().get(current_char, -INFINITY)
                log_value = transition_probability + matrix.get(state, position - 1) + emission_value
                state_values[dst_state].append((log_value, state))
        # after iterating through all states and all possible transitions we get the best and add them to the matrix
        for dst_state, value_tuple_list in state_values.iteritems():
            if len(value_tuple_list) > 0:
                value, state = max(value_tuple_list) # by default uses the first item to compute the max
                matrix.set(dst_state, position, value)
                matrix.connect((dst_state, position), (state, position - 1))
            else:
                matrix.set(dst_state, position, -INFINITY)

    print matrix
    # TODO: get best sequence of states!!! (fill it)
