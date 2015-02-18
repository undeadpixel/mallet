class Alignment:
    """
    Class including some interesting functions to create the
    output file mallet.
    """

    def __init__(self, sequence, state_path, score):
        self.score = score
        self.sequence = sequence
        self.state_path = state_path

    #Other functions:

    def __len__(self):
        """Return the length of a sequence/path"""
        return len(self.sequence)

    def __eq__(self, other_alignment):
        """
        Compare the score, path and sequence of two sequences and
        return a list of booleans.
        """
        x = self.score == other_alignment.score
        y = self.sequence == other_alignment.sequence
        z = self.state_path == other_alignment.state_path
        return x and y and z

    def __repr__(self):
        return "Score: {:.4f}\nSequence:\n{}\nPath:\n{}\n\n".format(self.score, self.sequence, self.state_path)
