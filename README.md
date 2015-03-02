# Mallet

## Introduction

Mallet is a simple implementation of the viterbi algorithm for scoring a set of sequences (for example DNA, RNA or protein) by their structure using Hidden Markov Models.

It also has additional features, such as a HMM sampler, a position frequence counter and entropy-based stats.

It has been implemented by Josep Arús and Samuel Miravet as a project for the Advanced Genome Bioinformatics (AGB) subject in the MSc in Bioinformatics at the [Universitat Pompeu Fabra](http://www.upf.edu).

For a step-by-step guide with examples, please refer to the [user's guide](https://github.com/undeadpixel/mallet/wiki).

## Command-line reference

Mallet is used by calling the `mallet.py` file in the main folder. You will have to specify an action with correct args.

### Input formats

Input format definition for HMMs and sequence lists.

#### TGF

Hidden Markov models are to be codified in an extended version of the TGF (trivial graph format) format.

This format has 3 blocks: state definition, transitions and emissions.
Each block is separated from the previous by a single `#` (you can add text after, is ignored).
Lines starting with a `;` are ignored (comments).

The first block, state definitions, are the definitions of each state comprised of an ID, a descriptive name and a short one-letter name. It has to include a BEGIN state and an END state, else the HMM would'nt be complete.
The second block uses the identifiers from the first and adds a probability on each transition.
The third block also uses the identifiers from the first and adds probabilities for each emission.

**Note:** Each state emissions and transitions must sum 1.0.

**Example**

    ; a simple HMM
    1 Begin BEGIN
    2 State1 S
    3 State2 T
    4 End END
    # Transitions
    1 2 1.0
    ; some random comment
    2 2 0.5
    2 3 0.5
    3 3 0.4
    3 4 0.6
    # Emissions
    2 A 0.3
    2 B 0.7
    3 A 1.0
    ; emissions not specified have probability 0

#### Sequences

Sequences can be specified using one of the two options:

* **RAW**: `file_name.raw` Sequences separated by endlines.
* **FASTA** `file_name.raw` A standard FASTA file.

### Output format

#### MALLET

Alignments from viterbi are given in MALLET format. The specification is very simple:

      # SEQUENCE_NAME
      # SCORE
      
      TCTACCAACAAGAATGAGCTTGAAAGCAGATTCTTCCCTCGCACTTAAAGGTGAGTACTTTTAGCCTGGCCAACACCTTC
      EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE234*67890IIIIIIIIIIIIIIIIIIIIIIII
      
      ATTTCA
      IIIIII

Alignment is partitioned in chunks of 80 characters.

### Actions

Here are the different actions the program can execute.

#### viterbi

    mallet.py viterbi HMM_TGF_FILE SEQUENCES_FILE [OUTPUT_MALLET_FILE]

Runs viterbi algorithm on all the sequences in the file with the given HMM. It returns a MALLET file with the alignments.

When output is not given, it prints the mallet file through stdout.

#### sample

    mallet.py sample LENGTH HMM_TGF_FILE [OUTPUT_MALLET_FILE]

Returns a sample alignment of `max_lenght = LENGTH` in MALLET format.

When output is not given, it prints the mallet file through stdout.

#### frequencies

    mallet.py frequencies SEQUENCES_FILE ALPHABET [OUTPUT_TSV_FILE] [--pseudocounts]

Returns a TSV of the frequencies of each symbol of the given alphabet for all the sequences in the file. Note that all the sequence have to be of equal lenght, else the algorithm won't work. You can specify pseudocounts with the `--pseudocounts` option.

**Note:** Alphabet is specified as a string with all the symbols (i.e: DNA would have "CGAT"). Order is not important.

When output is not given, it prints the TSV file through stdout.

#### sequence_stats

    mallet.py mallet.py sequence_stats SEQUENCES_FILE ALPHABET [OUTPUT_TSV_FILE]

Returns a TSV with the adjacent position entropy-based metrics (ie: 1-2, 2-3, 3-4 ...). The metrics given are:
jensen_shannon	joint_entropy	mutual_information	mutual_information_distance	mutual_information_ratio
* Jensen-Shannon distance
* Joint entropy
* Mutual information
* [Mutual information distance](http://en.wikipedia.org/wiki/Mutual_information#Metric) aka. Variation of information.
* Mutual information ratio (Normalized version of the MI, not very useful though...)

**Note:** Alphabet is specified as a string with all the symbols (i.e: DNA would have "CGAT"). Order is not important.

When output is not given, it prints the TSV file through stdout.

## Usage as a library

Mallet can also be used as a library. Better read the source code, but a simple example of a script that runs Viterbi:

``` python
import mallet.input.sequence_parser as seq_parser
import mallet.input.tgf_parser as tgf_parser
import mallet.viterbi as viterbi

hmm = tgf_parser.parse(hmm_file)
sequences = seq_parser.parse(sequences_file)

alignments = viterbi.viterbi_all(hmm, sequences)

# do whatever you like with the alignments ....
```

There are some scripts in the utils section.
