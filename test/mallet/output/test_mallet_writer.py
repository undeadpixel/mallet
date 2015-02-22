import test.helpers as helpers
import nose.tools as nt

import test.fixtures.alignment_fixtures as fixtures

import mallet.sequence as seq
import mallet.output.mallet_writer as mallet_writer

tmp_output_filename = "/tmp/output.mallet"

class TestSequenceParser(object):

    def subject(self, alignments = None):
        if alignments is None: alignments = fixtures.alignments()
        mallet_writer.write(alignments, tmp_output_filename)

    def assert_output(self, output):
        helpers.assert_file_contents("test/files/{}".format(output), tmp_output_filename)

    def test_empty_list(self):
        self.subject([])
        self.assert_output("empty")

    def test_sample_list(self):
        self.subject()
        self.assert_output("mallet/sample.mallet")

    def test_list_with_none_states(self):
        self.subject(fixtures.none_state_alignments())
        self.assert_output("mallet/none_states.mallet")

    def test_list_with_long_alignments(self):
        self.subject(fixtures.long_alignments())
        self.assert_output("mallet/long_alignments.mallet")

