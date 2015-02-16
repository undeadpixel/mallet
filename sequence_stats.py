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

def position_freqs(sequences, monomers):
  num_positions = len(sequences[0])
  frequencies = dict((position, dict((monomer, 0.0) for monomer in monomers)) for position in range(num_positions))

  for position in range(num_positions):
    for sequence in sequences:
      monomer = sequence[position]
      frequencies[position][monomer] += 1

  num_sequences = len(sequences)
  for position,monomers in frequencies.iteritems():
    for monomer,count in monomers.iteritems():
      frequencies[position][monomer] /= num_sequences

  return frequencies

def joint_frequencies(sequences, monomers):
  num_positions = len(sequences[0])
  frequencies = {}
  for position in range(num_positions - 1):
    frequencies[(position, position + 1)] = {}
    for monomer in monomers:
      for other_monomer in monomers:
        frequencies[(position, position + 1)][(monomer, other_monomer)] = 0.0

  for position in range(num_positions - 1):
    for monomer in monomers:
      for other_monomer in monomers:
        for sequence in sequences:
          current_monomer = sequence[position]
          next_monomer = sequence[position + 1]
          if current_monomer == monomer and next_monomer == other_monomer:
            frequencies[(position, position + 1)][(monomer, other_monomer)] += 1

  num_sequences = len(sequences)
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

        if frequency_x != 0.0 and frequency_y != 0.0 and joint_frequency != 0.0:
          results[position_key] += joint_frequency*math.log(joint_frequency/(frequency_x*frequency_y), 2)

  return results

def shannon_divergence(frequencies):
  num_positions = len(sequences[0])
  results = dict(((position, position + 1), 0.0) for position in range(num_positions - 1))

  for position in range(num_positions - 1):
    next_position = position + 1
    position_key = (position, next_position)

    for monomer in monomers:
      p_x = frequencies[position][monomer]
      q_x = frequencies[position + 1][monomer]
      if p_x != 0 and q_x != 0:
        sum_p_x = p_x*math.log(2*p_x/(p_x + q_x), 2)
        sum_q_x = q_x*math.log(2*q_x/(p_x + q_x), 2)
        results[position_key] += 0.5*(sum_p_x + sum_q_x)

  return results

if __name__ == "__main__":
  in_filename, monomers = parse_args()
  sequences = seq_parser.parse(in_filename)

  frequencies = position_freqs(sequences, monomers)
  joint_frequencies = joint_frequencies(sequences, monomers)

  mutual_informations = mutual_information(frequencies, joint_frequencies)
  jensen_shannon = shannon_divergence(frequencies)
  
  for positions, js in jensen_shannon.iteritems():
    print "{} : {:.4f}".format(positions, js)
