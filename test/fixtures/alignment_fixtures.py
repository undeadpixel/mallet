from mallet.sequence import Sequence
from mallet.alignment import Alignment

def alignments():
    return [
        Alignment(Sequence("P1", "ABABABA"), Sequence("State path", "STTTTTU"), -12.34),
        Alignment(Sequence("P2", "ABA"), Sequence("State path", "STU"), -1.56),
        Alignment(Sequence("P3", "AAAB"), Sequence("State path", "SSSU"), -2.78)
    ]

def none_state_alignments():
    return [
        Alignment(Sequence("P1", "AAAB"), None, -2.78),
        Alignment(Sequence("P2", "ABA"), Sequence("State path", "STU"), -1.56),
    ]

def long_alignments():
    return [
        Alignment(Sequence("P1", "ABA"*80), Sequence("State path", "STU"*80), -1.56),
        Alignment(Sequence("P2", "AA"*76), Sequence("State path", "SU"*76), 45.56),
    ]

def none_score_alignments():
    return [
        Alignment(Sequence("P1", "ABABABA"), Sequence("State path", "STTTTTU"), -12.34),
        Alignment(Sequence("P2", "ABA"), Sequence("State path", "STU"), None),
        Alignment(Sequence("P3", "AAAB"), Sequence("State path", "SSSU"), None)
    ]

