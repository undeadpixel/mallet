import nose.tools as nt

def assert_type(object, klass):
    nt.assert_equals(type(object), klass)

def assert_file_contents(filename_1, filename_2):
    with open(filename_1, 'r') as file:
        file_1_contents = file.read()
    with open(filename_2, 'r') as file:
        file_2_contents = file.read()

    nt.assert_equals(file_1_contents, file_2_contents)
