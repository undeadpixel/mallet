import sequence as seq

INF = float('inf')

def viterbi_all(hmm, sequences):
    """
    Runs the viterbi algorithm on a list of sequences given a Hidden Markov Model.
    """
    results = []
    for sequence in sequences:
        results.append(viterbi(hmm, sequence))
    return results

# CRAB VITERBI :)
def viterbi(hmm, sequence):
    """
    Given a sequence and a HMM, returns the maximal state path.
    """
    state_path = seq.Sequence("State path", "")
    states = hmm.states.values()

    # initialize matrix with all -inf
    matrix = ViterbiMatrix(states, sequence, -INF)
    # states have -inf in sequence gap
    for state in states:
        matrix.set(state, "-", -INF)
    # all in state begin have -inf except first
    for char in sequence:
        matrix.set(hmm.begin_state(), char, -INF)
    # initialize matrix with state begin and sequence gap = 0
    matrix.set(hmm.begin_state(), "-", 0.0)

    previous_char = "-"
    for char in sequence:
        state_probabilities = dict((state, []) for state in states)
        for state in states:
            for dst_state,trans_prob in state.transitions.iteritems():
                value = trans_prob + matrix.get(state, previous_char) + dst_state.emissions[char]
                state_probabilities[dst_state].append((value, state))
        # maximise state probabilities
        for state,list_values in state_probabilities:
            # max has to be with a lambda
            value = max(lambda: ..., list_values)
            matrix.set(state, char, value[0])
            matrix.connect(state, char, value[1], previous_char)
        previous_char = char



class ViterbiMatrix(object):

    def __init__(self, states, sequence):
        self.__states = states
        self.__sequence = sequence
        self.__initialize_matrix(states, sequence)

    def get(self, i, j):
        pass

    def set(self, i, j, value):
        pass

    def connect(self, i, j, k, l):
        parent = self.get(i,j)
        child = self.get(k,l)
        child.parent = parent

    # private

    def __initialize_matrix(self, states, sequence):
        self.matrix = []
        for state in states:
            self.matrix.append()

class ViterbiElement(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
