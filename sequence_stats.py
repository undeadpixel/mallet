#!/usr/bin/env python

import sys
import math

import mallet.input.sequence_parser as seq_parser

def parse_args():
    if len(sys.argv) < 2:
        raise RuntimeError("Invalid arguments")

    filename = sys.argv[1]
    monomers = sys.argv[2]

    return (filename, monomers)

def position_freqs(sequences, monomers, with_pseudocounts = False):

    start_count = 0.0
    if with_pseudocounts: start_count = 1.0

    num_positions = len(sequences[0])

    # initialize frequencies dictionary
    frequencies = dict((position, dict((monomer, start_count) for monomer in monomers)) for position in range(num_positions))

    # count matches
    for position in range(num_positions):
        for sequence in sequences:
            monomer = sequence[position]
            frequencies[position][monomer] += 1

    num_sequences = len(sequences)
    if with_pseudocounts: num_sequences += len(monomers)

    # obtain probabilities
    for position,monomers in frequencies.iteritems():
        for monomer,count in monomers.iteritems():
            frequencies[position][monomer] /= num_sequences

    return frequencies

def joint_frequencies(sequences, monomers, with_pseudocounts = False):
    start_count = 0.0
    if with_pseudocounts: start_count = 1.0


    num_positions = len(sequences[0])

    # initialization of frequencies dictionary
    frequencies = {}
    for position in range(num_positions - 1):
        frequencies[(position, position + 1)] = {}
        for monomer in monomers:
            for other_monomer in monomers:
                frequencies[(position, position + 1)][(monomer, other_monomer)] = start_count

    # count all matches
    for position in range(num_positions - 1):
        for monomer in monomers:
            for other_monomer in monomers:
                for sequence in sequences:
                    current_monomer = sequence[position]
                    next_monomer = sequence[position + 1]
                    if current_monomer == monomer and next_monomer == other_monomer:
                        frequencies[(position, position + 1)][(monomer, other_monomer)] += 1

    # obtain probabilities
    num_sequences = len(sequences)
    if with_pseudocounts: num_sequences += len(monomers)**2
    for position in range(num_positions - 1):
        for monomer in monomers:
            for other_monomer in monomers:
                frequencies[(position, position + 1)][(monomer, other_monomer)] /= num_sequences

    return frequencies


def mutual_information(frequencies, joint_frequencies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        for monomer in monomers:
            for other_monomer in monomers:
                frequency_x = frequencies[position][monomer]
                frequency_y = frequencies[position + 1][other_monomer]
                joint_frequency = joint_frequencies[position_key][(monomer, other_monomer)]

                results[position_key] += joint_frequency*safe_log2(safe_div(joint_frequency, (frequency_x*frequency_y)))

    return results

def joint_entropy(joint_frequencies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        for monomer in monomers:
            for other_monomer in monomers:
                joint_frequency = joint_frequencies[position_key][(monomer, other_monomer)]

                results[position_key] -= joint_frequency*safe_log2(joint_frequency)

    return results

def mi_distance(mutual_informations, joint_entropies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        results[position_key] = joint_entropies[position_key] - mutual_informations[position_key]

    return results

def mi_ratio(mutual_informations, joint_entropies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        if joint_entropies[position_key] != 0.0:
            results[position_key] =  mutual_informations[position_key]/joint_entropies[position_key]
        else:
            results[position_key] = 1.0

    return results

def shannon_divergence(frequencies):

    def shannon_factor(p,q):
        return p*safe_log2(safe_div(2*p, (p + q)))

    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        for monomer in monomers:
            p_x = frequencies[position][monomer]
            q_x = frequencies[position + 1][monomer]
            results[position_key] += 0.5*(shannon_factor(p_x, q_x) + shannon_factor(q_x, p_x))

    for position_key,value in results.iteritems():
        results[position_key] = math.sqrt(value)

    return results

def print_positions_list(positions_list):
    positions_list = positions_list.items()
    positions_list = sorted(positions_list)

    for positions,value in positions_list:
        print "{} - {:.04f}".format(positions, value)

def print_csv(mi_distances, jensen_shannons):

    with open("output.csv", "w") as out_fd:
        out_fd.write("position\tmi_distance\tjensen_shannon_distance\n")
        keys = mi_distances.keys()
        keys = sorted(keys)
        for positions in keys:
            new_positions = (positions[0] + 1, positions[1]+1)
            out_fd.write("{}\t{:.4f}\t{:.4f}\n".format(new_positions, mi_distances[positions], jensen_shannons[positions]))

def safe_log2(value):
    if value == 0.0: value = 1e-50
    return math.log(value, 2)

def safe_div(numerator, denominator):
    if denominator == 0.0: denominator = 1e-50
    return numerator/denominator

if __name__ == "__main__":
    in_filename, monomers = parse_args()
    sequences = seq_parser.parse(in_filename)

    frequencies = position_freqs(sequences, monomers)
    joint_frequencies = joint_frequencies(sequences, monomers)

    mutual_informations = mutual_information(frequencies, joint_frequencies)
    joint_entropies = joint_entropy(joint_frequencies)
    mi_distances = mi_distance(mutual_informations, joint_entropies)
    mi_ratios = mi_ratio(mutual_informations, joint_entropies)
    jensen_shannons = shannon_divergence(frequencies)
    
    print "> Mutual Information"
    print_positions_list(mutual_informations)

    print "> Joint Entropy"
    print_positions_list(joint_entropies)

    # print "> Mutual Information distances"
    # print_positions_list(mi_distances)
    print "> Mutual Information ratios"
    print_positions_list(mi_ratios)
    # print "> Jensen-Shannon"
    # print_positions_list(jensen_shannons)

    print_csv(mi_distances, jensen_shannons)
