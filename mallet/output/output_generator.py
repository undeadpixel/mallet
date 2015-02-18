#!/usr/bin/env python

import gzip
import sys

#TODO pass the output file by arguments

def output_file_generator(results_list, outfile=None):
    """
    Given a list of output_alignment objects, generate an output file.
    If the output ends with .gz, generate a compressed file.
    If no output defined, print the results in the command line.
    """
    if outfile is None:
        for output_object in results_list:
            sys.stdout.write(repr(output_object))

    elif outfile.endswith(".gz"):
        with gzip.open(outfile, "wb") as o:
            for output_object in results_list:
                o.write(repr(output_object).encode('utf-8'))

    else:
        with open(outfile, 'w') as o:
            for output_object in results_list:
                o.write(repr(output_object))


