import mallet.sequence as seq

def sequences():
    return [
        seq.Sequence("S1", "ABCABCABC"),
        seq.Sequence("S2", "AAAAA"),
        seq.Sequence("S3", "CBCBCBCBC")
    ]

def long_sequences():
    return [
        seq.Sequence("L1", "A"*800),
        seq.Sequence("L2", "ABCA"*123),
    ]
