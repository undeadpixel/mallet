import sys
import math

import safe_math

# TODO: Unit testing

def position_frequencies(sequences, alphabet, with_pseudocounts = False):

    start_count = 0.0
    if with_pseudocounts: start_count = 1.0

    num_positions = len(sequences[0])

    # initialize frequencies dictionary
    frequencies = dict((position, dict((monomer, start_count) for monomer in alphabet)) for position in range(num_positions))

    # count matches
    for position in range(num_positions):
        for sequence in sequences:
            monomer = sequence[position]
            frequencies[position][monomer] += 1

    num_sequences = len(sequences)
    if with_pseudocounts: num_sequences += len(alphabet)

    # obtain probabilities
    for position,alphabet in frequencies.iteritems():
        for monomer,count in alphabet.iteritems():
            frequencies[position][monomer] /= num_sequences

    return frequencies

def joint_frequencies(sequences, alphabet, with_pseudocounts = False):
    start_count = 0.0
    if with_pseudocounts: start_count = 1.0

    num_positions = len(sequences[0])

    # initialization of frequencies dictionary
    frequencies = {}
    for position in range(num_positions - 1):
        frequencies[(position, position + 1)] = {}
        for monomer in alphabet:
            for other_monomer in alphabet:
                frequencies[(position, position + 1)][(monomer, other_monomer)] = start_count

    # count all matches
    for position in range(num_positions - 1):
        for monomer in alphabet:
            for other_monomer in alphabet:
                for sequence in sequences:
                    current_monomer = sequence[position]
                    next_monomer = sequence[position + 1]
                    if current_monomer == monomer and next_monomer == other_monomer:
                        frequencies[(position, position + 1)][(monomer, other_monomer)] += 1

    # obtain probabilities
    num_sequences = len(sequences)
    if with_pseudocounts: num_sequences += len(alphabet)**2
    for position in range(num_positions - 1):
        for monomer in alphabet:
            for other_monomer in alphabet:
                frequencies[(position, position + 1)][(monomer, other_monomer)] /= num_sequences

    return frequencies


def mutual_information(sequences, alphabet, frequencies, joint_frequencies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        for monomer in alphabet:
            for other_monomer in alphabet:
                frequency_x = frequencies[position][monomer]
                frequency_y = frequencies[position + 1][other_monomer]
                joint_frequency = joint_frequencies[position_key][(monomer, other_monomer)]

                results[position_key] += joint_frequency*safe_math.log2(safe_math.div(joint_frequency, (frequency_x*frequency_y)))

    return results

def joint_entropy(sequences, alphabet, joint_frequencies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        for monomer in alphabet:
            for other_monomer in alphabet:
                joint_frequency = joint_frequencies[position_key][(monomer, other_monomer)]

                results[position_key] -= joint_frequency*safe_math.log2(joint_frequency)

    return results

def mutual_information_distance(sequences, mutual_informations, joint_entropies):
    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        results[position_key] = joint_entropies[position_key] - mutual_informations[position_key]

    return results

def mutual_information_ratio(sequences, mutual_informations, joint_entropies):
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

def shannon_divergence(sequences, alphabet, frequencies):

    def shannon_factor(p,q):
        return p*safe_math.log2(safe_math.div(2*p, (p + q)))

    num_positions = len(sequences[0])
    results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

    for position in range(num_positions - 1):
        next_position = position + 1
        position_key = (position, next_position)

        for monomer in alphabet:
            p_x = frequencies[position][monomer]
            q_x = frequencies[position + 1][monomer]
            results[position_key] += 0.5*(shannon_factor(p_x, q_x) + shannon_factor(q_x, p_x))

    for position_key,value in results.iteritems():
        results[position_key] = math.sqrt(value)

    return results

def all_stats(sequences, alphabet):
    frequencies = position_frequencies(sequences, alphabet)
    joint_freqs = joint_frequencies(sequences, alphabet)

    mutual_informations = mutual_information(sequences, alphabet, frequencies, joint_freqs)
    joint_entropies = joint_entropy(sequences, alphabet, joint_freqs)
    mi_distances = mutual_information_distance(sequences, mutual_informations, joint_entropies)
    mi_ratios = mutual_information_ratio(sequences, mutual_informations, joint_entropies)
    jensen_shannons = shannon_divergence(sequences, alphabet, frequencies)

    return {
        'mutual_information': mutual_informations,
        'joint_entropy': joint_entropies,
        'mutual_information_distance': mi_distances,
        'mutual_information_ratio': mi_ratios,
        'jensen_shannon': jensen_shannons
    }

