import gzip, sys, re


def write(alignments, out_filename = None):
    """
    Given a list of output_alignment objects, generate an output file.
    If the output ends with .gz, generate a compressed file.
    If no output defined, print the results in the command line.
    """

    def partition_sequence(sequence):
        chunks = re.split("(.{80})", sequence) # split in 80 char chunks
        return filter(None, chunks) # remove empty chunks

    def format_alignment(alignment):
        output = "# {}\n".format(alignment.sequence.identifier)
        if alignment.state_path:
            if alignment.score:
                output += "# {:.4f}\n".format(alignment.score)
            output += "\n"
        else:
            output += "# -\n\n"

        # divide alignment and state path in 80 char chunks
        partitioned_sequence = partition_sequence(alignment.sequence.sequence)
        if alignment.state_path:
            partitioned_state_path = partition_sequence(alignment.state_path.sequence)
        for chunk in range(len(partitioned_sequence)):
            output += "{}\n".format(partitioned_sequence[chunk])
            if alignment.state_path:
                output += "{}\n".format(partitioned_state_path[chunk])
            output += "\n"

        return output


    write_bytes = lambda text: fd.write(text.encode('utf-8'))
    write_text = lambda text: fd.write(text)

    write_function = write_text

    fd = sys.stdout
    if out_filename is not None:
        if out_filename.endswith('.gz'):
            fd = gzip.open(out_filename, 'wb')
            write_function = write_bytes
        else:
            fd = open(out_filename, 'w')

    for alignment in alignments:
        write_function(format_alignment(alignment))

    fd.close()
