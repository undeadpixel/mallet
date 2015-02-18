import gzip
import sys

def write(alignments, out_filename = None):
    """
    Given a list of output_alignment objects, generate an output file.
    If the output ends with .gz, generate a compressed file.
    If no output defined, print the results in the command line.
    """

    # TODO: write real MALLET file
    def format_alignment(alignment):
        repr(alignment)

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
        # TODO: write real MALLET file
        write_function(format_alignment(alignment))

    fd.close()
