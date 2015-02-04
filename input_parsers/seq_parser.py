def FASTA_iterator( fasta_filename ):
    """"A Generator function that reads a FASTA file.
    In each iteration, the function returns a
    tuple with the  following format: (identifier, sequence).

    """

    fasta_file = open(fasta_filename, 'r')

    identifier = ""
    completeseq = []

    for line in fasta_file:
        line = line.strip()
        if line.startswith(">"):
            if completeseq:
                yield (identifier, ''.join(completeseq))
                completeseq = []
            identifier = line[1:]
        else:
            completeseq.append(line)

    fasta_file.close()

    if len(''.join(completeseq)) > 0:
        yield (identifier, ''.join(completeseq))

def raw_seq_iterator(seqs_filename):
    """A Generator function that reads a file with raw
    sequences. In each iteration, the function returns a
    string with the sequence.

    """
    with open(seqs_filename, "r") as seqs_file:
        for line in seqs_file:
            line = line.strip()
            yield line
