import mallet.viterbi as viterbi
import mallet.sequence as seq
import mallet.input.tgf_parser as tgf
import mallet.input.sequence_parser as seq_parser

sequences = seq_parser.parse("files/sequences/context_real_donors.raw")
hmm = tgf.parse("files/hmms/toy_model.tgf")

correct_state_path = seq.Sequence("State path", "E"*50 + "5" + "I"*35)

def print_percent(number):
    print "{:.4f} %".format(number*100.0)

def process_sequences():
    alignments = viterbi.viterbi_all(hmm, sequences)
    # return alignments
    valid_alignments = filter(lambda align: align.state_path == correct_state_path, alignments)

    return (alignments, valid_alignments)

if __name__ == '__main__':
    alignments, valid_alignments = process_sequences()

    sensitivity = float(len(valid_alignments))/len(alignments)
    print_percent(sensitivity)

    # for alignment in alignments:
    #     print alignment
