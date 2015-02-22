class Alignment(object):
    """
    Class including some interesting functions to create the
    output file mallet.
    """

    def __init__(self, sequence, state_path, score = None):
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
        output = ""
        if self.score:
            output += "[{:.4f}]".format(self.score)
        else:
            output += "[-]"
        output += "[{}|".format(self.sequence.sequence)

        if self.state_path:
            output += "{}]".format(self.state_path.sequence)
        else:
            output += "-]"
        return output
        # return "Score: {:.4f}\nSequence:\n{}\nPath:\n{}\n\n".format(self.score, self.sequence, self.state_path)
