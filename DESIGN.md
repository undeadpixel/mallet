# Main behaviour

Given a set of sequences in different formats (FASTA, line-by-line) and a Hidden Markov Model in an **extended** version of the [Trivial Graph Format](http://en.wikipedia.org/wiki/Trivial_Graph_Format), it returns the best state path for each sequence and its score in a file.

# Definition of our version of TGF

    1 DESCR CODE
    ...
    N DESCR CODE
    #
    1 1 PROB
    1 2 PROB
    #
    1 A PROB
    1 B PROB
    2 A PROB
    ...

TODO

# Description of the CMD interface

    -sequence seq.fasta

    -true_sequence true.fasta
    -false_sequence false.fasta
    -true_state_path true.states
    -false_state_path false.states

TODO

# Definition of the MAUL format


    > SEQ: NAME_SEQ

    > ALIGNMENT: 1
    > SCORE: -432
    SEQUENCESEQUENCESEQUENCESEQ
    STATEPATHSTATEPATHSTATEPATH

    SEQUENCESEQUENCESEQUENCESEQ
    STATEPATHSTATEPATHSTATEPATH

    > ALIGNMENT: 2
    > SCORE: -463
    SEQUENCESEQUENCESEQUENCESEQ
    STATEPATHSTATEPATHSTATEPATH

    SEQUENCESEQUENCESEQUENCESEQ
    STATEPATHSTATEPATHSTATEPATH

    > ALIGNMENT: 3
    > SCORE: -481
    SEQUENCESEQUENCESEQUENCESEQ
    STATEPATHSTATEPATHSTATEPATH

    SEQUENCESEQUENCESEQUENCESEQ
    STATEPATHSTATEPATHSTATEPATH

    > SEQ: NAME_SEQ2

    ...

# Modules

  + **Input management:** Convert input format into internal representations.
    + TGF parser
    + FASTA parser
    + Line-by-line parser
    + MAUL parser
    + Command line args parser (\*)
  + **Algorithm:** 
    + Implementation of the Viterbi algorithm using internal representations of input data.
    + Implementation of a sample algorithm (Given a set of state paths it returns sequences)
  + **Quality assesment:** Implement Sensitivity, specificity and accuracy.
  + **Output management:** Return results from the internal representation Viterbi generates.
  + Testing

# Some ideas...

    TGF -> Graph
    FASTA o LbL *-> Sequence
    MAUL *-> StatePath(Sequence)

    Sequence *-> Viterbi *-> StatePath(Sequence)
    StatePath(Sequence) + StatePath(Sequence) *-> Quality assessment -> QualityAssessmentResults(StatePath) (\*)

    StatePath *-> OUTPUT -> file, stdout ...
    QualityAssessmentResults *-> OUTPUT -> file, stdout
