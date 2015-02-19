#!/usr/bin/env python

import sys

import mallet.sample as sample
import mallet.viterbi as viterbi
import mallet.input.tgf_parser as tgf
import mallet.input.sequence_parser as seq_parser
import mallet.output.mallet_writer as mallet_writer

def parse_args():
    if len(sys.argv) < 2:
        raise RuntimeError("Invalid arguments")

    if sys.argv[1] == '-h':
        print """
HELP MESSAGE PENDING
        """
        sys.exit(0)

    action = sys.argv[1]
    args = sys.argv[2:]

    return (action, args)

if __name__ == '__main__':
    action, args = parse_args()

    if action == 'sample':
        hmm = tgf.parse(args[1])
        length_of_sample = int(args[0])

        print sample.sample(hmm, length_of_sample)

    if action == 'viterbi':
        hmm = tgf.parse(args[0])
        sequences = seq_parser.parse(args[1])

        mallet_writer.write(viterbi.viterbi_all(hmm, sequences))
