import mallet.viterbi as viterbi
import mallet.sequence as seq
import mallet.input.tgf_parser as tgf
import mallet.input.sequence_parser as seq_parser

sequences = seq_parser.parse("files/sequences/tia1_calculation/test_tia1.raw")
# hmm = tgf.parse("files/hmms/u1_binding_tgf/u1_complete.tgf")
# hmm = tgf.parse("files/hmms/u1_binding_tgf/u1_2_8.tgf")
# hmm = tgf.parse("files/hmms/u1_binding_tgf/u1_3_7.tgf")
# hmm = tgf.parse("files/hmms/tia1_binding_tgf/tia1_binding.tgf")
hmm = tgf.parse("files/hmms/tia1_binding_tgf/u1_tia1_binding.tgf")

# correct_state_path = seq.Sequence("State path", "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE234*67890IIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
# correct_state_path = seq.Sequence("State path", "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE34*6789IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
# correct_state_path = seq.Sequence("State path", "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE4*678IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

correct_state_path_fragment = "34*6789"

def print_percent(number):
    print "{:.4f} %".format(number*100.0)

def process_sequences():
    alignments = viterbi.viterbi_all(hmm, sequences)
    # return alignments
    valid_alignments = filter(lambda align: align.state_path.sequence[48:55] == correct_state_path_fragment, alignments)

    return (alignments, valid_alignments)

if __name__ == '__main__':
    alignments, valid_alignments = process_sequences()

    sensitivity = float(len(valid_alignments))/len(alignments)
    print_percent(sensitivity)

    # for alignment in alignments:
    #     print alignment
