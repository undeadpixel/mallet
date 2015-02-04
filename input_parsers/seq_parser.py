# First we define two functions to iterate over the file

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

    seqs_filename.close()

# Process to detect if the file is FASTA or raw and generate the class:

def sequence_generator(input_file):
    """Detects the type of input: raw or FASTA file and it
    generate Sequence classes for each sequence

    """

    with open(input_file, "r") as filehandle:
        if ">" in filehandle:
            for identifier, sequence in FASTA_iterator(input_file):
                return Sequence(identifier, sequence)
        else:
            i = 1
            for sequence in raw_seq_iterator(input_file):
                return Sequence("seq "+i, sequence)
                i += 1

# Class definition:

class Sequence:

    def __init__(self, identifier, sequence):

        self.__identifier = identifier
        self.__sequence = sequence

    def get_identifier(self):
        return self.__identifier

    def get_sequence(self):
        return self.__sequence

    def __len__(self):
        return len(self.get_sequence())

    def __getitem__(self, i):
        return self.get_sequence()[int(i)]
