#!/usr/bin/env python

import sys

import mallet.sample as sample
import mallet.viterbi as viterbi
import mallet.sequence_stats as sequence_stats

import mallet.input.tgf_parser as tgf
import mallet.input.sequence_parser as seq_parser

import mallet.output.mallet_writer as mallet_writer
import mallet.output.tsv_writer as tsv_writer

HELP_MESSAGE = """Usage: mallet.py ACTION ARG1 ARG2 ...

ACTIONS:
  sample:
    Description: Samples one possible sequence from a given HMM.
    Usage: mallet.py sample LENGTH HMM_TGF_FILE [OUTPUT_MALLET_FILE]
        LENGTH: length of the sequence to sample.
        HMM_TGF_FILE: A TGF file with the HMM.
  viterbi:
    Description: Runs the viterbi maximisation algorithm to the given sequences
                 and returns the scores and alignments.
    Usage: mallet.py viterbi HMM_TGF_FILE SEQUENCES_FILE [OUTPUT_MALLET_FILE]
        HMM_TGF_FILE: A TGF file with the HMM.
        SEQUENCES_FILE: A RAW or FASTA file name with the sequences (view docs)
        OUTPUT_MALLET_FILE: (optional) A file where the output will be stored.
                            If the file ends with .gz it gzips the output.
                            (view docs for format)
  sequence_stats:
    Description: Returns a TSV with some positional metrics (see docs) for the
                 given sequences.
    Usage: mallet.py sequence_stats SEQUENCES_FILE ALPHABET [OUTPUT_TSV_FILE]
        SEQUENCES_FILE: A RAW or FASTA file name with the sequences (view docs)
        ALPHABET: A string with all the emissions (Example: "ACGT")
        OUTPUT_TSV_FILE: (optional) A TSV file where the output will be stored.
  frequencies:
    Description: Returns a TSV with the probability of each emission in each
                 position for the given sequences.
    Usage: mallet.py frequencies SEQUENCES_FILE ALPHABET [OUTPUT_TSV_FILE]
        SEQUENCES_FILE: A RAW or FASTA file name with the sequences (view docs)
        ALPHABET: A string with all the emissions (Example: "ACGT")
        OUTPUT_TSV_FILE: (optional) A TSV file where the output will be stored.
"""

def print_help_message(invalid = False):
    if invalid: print "Invalid usage, correct usage below:\n"

    print HELP_MESSAGE
    sys.exit(0)

def parse_args():
    if len(sys.argv) < 2 or '-h' in sys.argv:
        print_help_message()

    action = sys.argv[1]
    args = sys.argv[2:]

    return (action, args)

def get_output_filename_from_args(args, position):
    if len(args) > position:
        return args[position]

if __name__ == '__main__':
    action, args = parse_args()

    if action == 'sample':
        if len(args) < 2: print_help_message(invalid=True)

        hmm = tgf.parse(args[1])
        length_of_sample = int(args[0])
        output_filename = get_output_filename_from_args(args, 2)

        mallet_writer.write([sample.sample(hmm, length_of_sample)], output_filename)

    elif action == 'viterbi':
        if len(args) < 2: print_help_message(invalid=True)

        hmm = tgf.parse(args[0])
        sequences = seq_parser.parse(args[1])
        output_filename = get_output_filename_from_args(args, 2)

        mallet_writer.write(viterbi.viterbi_all(hmm, sequences), output_filename)

    elif action == 'sequence_stats':
        if len(args) < 2: print_help_message(invalid=True)

        sequences = seq_parser.parse(args[0])
        alphabet = args[1]
        output_filename = get_output_filename_from_args(args, 2)

        all_stats = sequence_stats.all_stats(sequences, alphabet)

        tsv_writer.write_stats(all_stats, output_filename)

    elif action == 'frequencies':
        if len(args) < 2: print_help_message(invalid=True)

        sequences = seq_parser.parse(args[0])
        alphabet = args[1]
        output_filename = get_output_filename_from_args(args, 2)

        emission_frequencies_per_position = sequence_stats.position_frequencies(sequences, alphabet)

        tsv_writer.write_emission_frequencies_per_position(emission_frequencies_per_position, output_filename)

    else: print_help_message(invalid=True)

