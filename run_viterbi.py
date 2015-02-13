import mallet.viterbi as viterbi
import mallet.input.tgf_parser as tgf

import mallet.sequence as seq

hmm = tgf.parse("test/files/sample1.tgf")

result = viterbi.viterbi(hmm, seq.Sequence("P1", "AAAAAAA"))
print result
