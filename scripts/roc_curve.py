#!/usr/bin/env python

import sys, math

# added prent directory to import path
sys.path.append("..")

import mallet.viterbi as viterbi
import mallet.input.sequence_parser as seq_parser
import mallet.input.tgf_parser as tgf_parser
import mallet.safe_math as safe_math

STEPS = 100

def frange(start, end, step):
    end += step # HACK: prevent floating point errors in end
    current = start
    while current <= end:
        yield current
        current += step

def float_floor(value, decimals = 1):
    value = value*(10**decimals)
    return math.floor(value)/(10**decimals)

def float_ceil(value, decimals = 1):
    value = value*(10**decimals)
    return math.ceil(value)/(10**decimals)

def evaluate_alignment(alignment):
    return (alignment, alignment.state_path.sequence[50] == "*")

def accuracy_metrics(evaluated_alignments, threshold):
    tp, tn, fp, fn = (0,0,0,0)
    for alignment,is_correct in evaluated_alignments:
        if alignment.score >= threshold:
            if is_correct:
                tp += 1
            else:
                fp += 1
        else:
            if is_correct:
                fn += 1
            else:
                tn += 1
    return (tp, tn, fp, fn)

def print_roc_data_in_tsv(roc_data):
    print "score\ttpr\tfpr\tppv\ttp\ttn\tfp\tfn"
    for score,metrics in sorted(roc_data.items()):
        print "{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}".format(score, *metrics)


hmm = tgf_parser.parse(sys.argv[1])
sequences = seq_parser.parse(sys.argv[2])

alignments = viterbi.viterbi_all(hmm, sequences)

evaluated_alignments = map(evaluate_alignment, alignments)

max_score = max(alignments, key = lambda align: align.score).score
min_score = min(alignments, key = lambda align: align.score).score

roc_data = {}

step_size = (max_score - min_score)/STEPS

scores_iterator = frange(float_floor(min_score), float_ceil(max_score), step_size)

for score in scores_iterator:
    tp, tn, fp, fn = accuracy_metrics(evaluated_alignments, score)

    tpr = safe_math.div(float(tp), float(tp+fn))
    fpr = safe_math.div(float(fp), float(fp+tn))
    ppv = safe_math.div(float(tp), float(tp+fp))

    roc_data[score] = (tpr, fpr, ppv, tp, tn, fp, fn)

print_roc_data_in_tsv(roc_data)
