import pdb
import sequence as seq
import alignment

INFINITY = float('inf')

class ViterbiMatrix(object):

    def __init__(self, hmm, sequence):
        self.hmm = hmm
        self.sequence = sequence

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

    def get_best_alignment(self):
        state_path = seq.Sequence("State path", "")
        current_cell = self.get_end_cell()
        score = current_cell.value
        if score > -INFINITY:
            current_cell = current_cell.parent
            while not current_cell.state.is_begin():
                state_path.append(current_cell.state.short_name)
                current_cell = current_cell.parent
            state_path.reverse()
        else:
            state_path = None
        return alignment.Alignment(self.sequence, state_path, score)

    def get_end_cell(self):
        return self.__get(self.hmm.end_state(), self.__sequence_length() - 1)

    def __repr__(self):
        output = "\t".join(["State"] + [str(i) for i in range(self.__sequence_length())]) + "\n"
        for state in sorted(self.__states(), lambda s,t: s.short_name == t.short_name ):
            array = self.matrix[state]
            output += "{}\t".format(state.short_name) + "\t".join([str(item) for item in array]) + "\n"
        return output

    # private

    def __states(self):
        return self.hmm.states.values()

    def __get(self, state, i):
        return self.matrix[state][i]

    def __sequence_length(self):
        return len(self.sequence) + 2

    def __initialize_matrix(self):
        def create_row(state):
            return [ViterbiMatrixCell(state, i) for i in range(self.__sequence_length())]
        self.matrix = dict((state, create_row(state)) for state in self.__states())

class ViterbiMatrixCell(object):

    def __init__(self, state, position):
        self.value = -INFINITY
        self.parent = None

        self.state = state
        self.position = position

    def __repr__(self):
        output = ""
        # if self.parent:
        #     output += "({})".format(self.parent.state.short_name)
        output += "{:.2f}".format(self.value)
        return output

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
    matrix = ViterbiMatrix(hmm, sequence)

    # Initialisation step
    matrix.set(hmm.begin_state(), 0, 0.0)

    # Recursion & termination steps
    for position in range(1, len(matrix_sequence)):
        current_char = matrix_sequence[position]

        # we save all probabilities for all states in a hash to then get the max for each state
        state_values = dict((state, []) for state in states)

        # Calculating all possible values for each cell
        for state in states:
            # as we don't have the anterior transitions but the posterior for each state, we have to do it the opposite way
            for dst_state,transition_value in state.log_transitions().iteritems():
                # get parent state cell value
                previous_state_value = matrix.get(state, position - 1)
                log_value = transition_value + previous_state_value
                # add emission value if not in the termination step
                if not dst_state.is_end():
                    # END state has no emissions
                    emission_value = dst_state.log_emissions().get(current_char, -INFINITY)
                    log_value += emission_value
                state_values[dst_state].append((log_value, state))

        # Maximisation step
        for dst_state, value_tuple_list in state_values.iteritems():
            if len(value_tuple_list) > 0:
                # calculate the max score
                value, state = max(value_tuple_list) # by default uses the first item of each tuple to compute the max
                # set the score in the matrix row
                matrix.set(dst_state, position, value)
                # connect the matrix row to its parent
                matrix.connect((dst_state, position), (state, position - 1))

    # Traceback step
    return matrix.get_best_alignment()
