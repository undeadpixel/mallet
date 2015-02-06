class Sequence:

    def __init__(self, identifier, sequence):
        self.identifier = identifier
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, i):
        return self.sequence[int(i)]

    def __eq__(self, other_sequence):
    	return self.sequence == other_sequence.sequence and self.identifier == other_sequence.identifier

