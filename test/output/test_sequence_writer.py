import mallet.test.helpers as helpers
import nose.tools as nt

import mallet.test.fixtures.sequence_fixtures as fixtures

import mallet.sequence as seq
import mallet.output.sequence_writer as sequence_writer

class TestSequenceWriter(object):

    def assert_output(self, other_filename):
        helpers.assert_file_contents(self.temp_file, "test/files/{}".format(other_filename))

class TestSequenceWriterFasta(TestSequenceWriter):

    temp_file = "/tmp/blah.fasta"

    def subject(self, sequences = fixtures.sequences(), filename = temp_file):
        sequence_writer.write_fasta(sequences, filename)

    # TESTS

    def test_writes_empty_list_of_sequences(self):
        self.subject(sequences = [])
        self.assert_output("empty")

    def test_writes_simple_list_of_sequences(self):
        self.subject()
        self.assert_output("simple_plain.fasta")

    def test_writes_really_long_sequences(self):
        self.subject(sequences = fixtures.long_sequences())
        self.assert_output("long_sequences.fasta")


class TestSequenceWriterRaw(TestSequenceWriter):

    temp_file = "/tmp/blah"

    def subject(self, sequences = fixtures.sequences(), filename = temp_file):
        sequence_writer.write_raw(sequences, filename)

    # TESTS

    def test_writes_empty_list_of_sequences(self):
        self.subject(sequences = [])
        self.assert_output("empty")

    def test_writes_simple_list_of_sequences(self):
        self.subject()
        self.assert_output("simple.raw")
