#!/usr/bin/env python

import sys

# added prent directory to import path
sys.path.append("..")

import mallet.viterbi as viterbi
import mallet.input.tgf_parser as tgf
import mallet.input.sequence_parser as seq_parser

def hmm_iterator(hmms, sequences):
    """
    Given a list of HMMs and a set of sequences, print the sensitivity, specifity and
    accuracy of the models.
    """

    for hmm in hmms:
        #Set values to zero
        sensitivity = 0
        specificity = 0
        accuracy = 0
        hmm_name = hmm.split("/")[-1].split(".")[0]

        #Parse tgf and run viterbi algorithm
        hmm = tgf.parse(hmm)
        alignments = viterbi.viterbi_all (hmm, sequences)

        #Compute true and false positives and false negatives
        true_positives = len(filter(lambda align: align.state_path[50] == "*", alignments))
        false_negatives = len(filter(lambda align: align.state_path[50] != "*", alignments))
        false_positives = false_negatives # True only for this concrete project!

        #Calculate sensitivity, specificity and accuracy
        sensitivity = float(true_positives)/(true_positives+false_negatives)
        specificity = float(true_positives)/(true_positives+false_positives)
        accuracy = (specificity + sensitivity)/2.0

        def print_percent(number):
            number = "{:.4f} %".format(number*100.0)
            return number

        print "{}\tSN: {}\tSP: {}\tavgSNSP: {}".format(hmm_name, print_percent(sensitivity), print_percent(specificity), print_percent(accuracy))

if __name__ == '__main__':

    #Sequences to test:
    sequences = seq_parser.parse("../files/sequences/context_real_donors.raw")

    #HMMS should include all the Hidden Markov Models to test"
    hmms = ("../files/hmms/toy_model.tgf",
            "../files/hmms/u1_binding_tgf/u1_complete.tgf",
            "../files/hmms/u1_binding_tgf/u1_2_8.tgf",
            "../files/hmms/u1_binding_tgf/u1_3_7.tgf",
            "../files/hmms/tia1_binding_tgf/small_prob_tia1.tgf",
            "../files/hmms/tia1_binding_tgf/small_prob_4TIA1.tgf",
            "../files/hmms/tia1_binding_tgf/comp_prob_tia1.tgf",
            "../files/hmms/tia1_binding_tgf/comp_prob_4tia1.tgf",
            )

    hmm_iterator(hmms, sequences)
