from pandas import *

#A previous function in order to get the sequences
def RAW_iterator(seqs_filename): 
    """
    A Generator function that reads a file with raw
    sequences. In each iteration, the function returns a
    string with the sequence.
    """
    with open(seqs_filename, "r") as seqs_file:
        for line in seqs_file:
            yield line
#Start the function to generate the profile:

def profile_matrix_creator( seqs_filename):

	'''Given a list of sequences, returns a profile matrix as a dictionary {'A': [5 1 0 0 ..], 'T': [0 0 3 5], 'C': etc.}'''

	seqlist = []
	for sequence in RAW_iterator(seqs_filename):
		seqlist.append(sequence)

	#1. First generate an empty hash
	profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
	
	#2. Iterate and generate the counts of each nt for each position
	for item in zip(*seqlist):
		for nt in ['A', 'C', 'G', 'T']:
			profile_matrix[nt].append(item.count(nt)/len(seqlist))

	return profile_matrix

#And the function to generate the consensus:

def consensus_string( profile_matrix ):
	'''This function returns a consensus string (a sequence for example) from a profile matrix'''
	
	consensus_seq = ''
	elements = tuple(profile_matrix.items())		#the method functions retrieve a list of tuples from a dictionary
	length = len(elements[0][1])
	for i in range(length):
		consensus_seq += max(elements, key = (lambda x: x[1][i]))[0]
	
	return consensus_seq


#Execution part:
x = profile_matrix_creator("./true_sequences.txt")
y = consensus_string(x)

print ("Consensus: {}".format(y))

df = DataFrame(x).T.fillna(0)
print (df)

with open("frequency_matrix.txt", 'w') as o:
    o.write(str(df))