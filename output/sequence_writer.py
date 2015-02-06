import re

import mallet.sequence as seq

def write_fasta(sequences, filename):
    """
    Writes a set of sequences to a given file in FASTA format.
    """
    with open(filename, 'w+') as file:
        for sequence in sequences:
            # partition the sequence in chunks of 80 chars
            partitioned_sequence = re.sub("(.{80})", "\\1\n", sequence.sequence).strip()
            # print FASTA representation
            file.write(">{}\n{}\n".format(sequence.identifier, partitioned_sequence))

def write_raw(sequences, filename):
    """
    Writes a set of sequences to a given file in RAW format.
    """
    with open(filename, 'w+') as file:
        for sequence in sequences:
            file.write("{}\n".format(sequence.sequence))
