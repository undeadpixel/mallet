#!/usr/bin/env python

import sys

import mallet.viterbi as viterbi
import mallet.input.tgf_parser as tgf
import mallet.input.sequence_parser as seq_parser

STEP = 0.1

start = 48
end = 55
path_range = "34*6789"

def frange(start, end, step):
    value = start
    while value < end:
        yield value
        value += step

def format_percent(number):
    return "{:.4f} %".format(number*100.0)

def compare_state_path(alignment):
    return alignment.state_path.sequence[start:end] == path_range

def compare_alignments(hmm, sequences, token = ""):
    alignments = viterbi.viterbi_all(hmm, sequences)
    valid_alignments = filter(compare_state_path, alignments)

    sensitivity = float(len(valid_alignments))/len(alignments)

    print "{} - {}".format(token, format_percent(sensitivity))

if __name__ == '__main__':

    sequences = seq_parser.parse(sys.argv[1])
    hmm = tgf.parse(sys.argv[2])

    # 10, 12, 13
    for probability10 in frange(0.0, 1.0, STEP):
        token = ""
        other_probability10 = 1.0 - probability10
        # change HMM
        hmm.states[10].set_transition_state(12, probability10)
        hmm.states[10].set_transition_state(13, other_probability10)

        token1 = "({:.4f},{:.4f})".format(probability10, other_probability10)
        
        transition_states_10 = hmm.states[10].transitions.keys()

        for probability12 in frange(0.0, 1.0, STEP):
            other_probability12 = 1.0 - probability12
            # change HMM
            hmm.states[12].set_transition_state(12, probability12)
            hmm.states[12].set_transition_state(13, other_probability12)

            token2 = token1 + "({:.4f},{:.4f})".format(probability12, other_probability12)

            transition_states_12 = hmm.states[12].transitions.keys()

            for probability13 in frange(0.0, 0.9, STEP):
                other_probability13 = 1.0 - probability13 - 0.1
                # change HMM
                hmm.states[13].set_transition_state(12, probability13)
                hmm.states[13].set_transition_state(13, other_probability13)

                token = token2 + "({:.4f},{:.4f})".format(probability13, other_probability13)
                # compare
                compare_alignments(hmm, sequences, token)
                
                transition_states_13 = sorted(hmm.states[13].transitions.keys(), key = lambda state: state.short_name)

    # compare_alignments(hmm, sequences)
