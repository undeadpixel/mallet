class output_alignment:
    """
    Class including some interesting functions to create the 
    output file mallet.
    """

    def __init__(self, score, sequence, path):
        self.score = score
        self.sequence = sequence
        self.path = path

    # Some getters:

    def get_score(self):
        return self.score

    def get_sequence(self):
        return self.sequence

    def get_path(self):
        return path

    #Other functions:

    def __len__(self):
        """Return the length of a sequence/path"""

        return len(self.sequence)

    def __get_sequence_item__(self, i):
        """
        Given an integer i, returns the value in the position i
        in the sequence.
        """
        return self.sequence[int(i)]

    def __get_path_item__(self, i):
        """
        Given an integer i, returns the value in the position i
        in the path.
        """
        return self.path[int(i)]

    def __eq__(self, other_output_alignment):
        """
        Compare the score, path and sequence of two sequences and
        return a list of booleans.
        """

        x = self.score == other_output_alignment.score
        y = self.sequence == other_output_alignment.sequence
        z = self.path == other_output_alignment.path

        return "#Same score: {} #Same sequence: {} #Same path: {}".format(x, y, z)

    def __repr__(self):
        return "Score: {}\nSequence:\n{}\nPath:\n{}\n\n".format(self.score, self.sequence, self.path)
