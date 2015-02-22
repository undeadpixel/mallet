import gzip

import nose.tools as nt

def assert_type(object, klass):
    nt.assert_equals(type(object), klass)

def assert_files(fd_1, fd_2):
    file_1_contents = fd_1.read()
    file_2_contents = fd_2.read()

    nt.assert_equals(file_1_contents, file_2_contents)

def assert_file_contents(filename_1, filename_2):
    with open(filename_1, 'r') as fd_1:
        with open(filename_2, 'r') as fd_2:
            assert_files(fd_1, fd_2)

def assert_gzipped_file_contents(filename, gzipped_filename):
    with open(filename, 'r') as fd_1:
        with gzip.open(gzipped_filename, 'r') as fd_2:
            assert_files(fd_1, fd_2)

