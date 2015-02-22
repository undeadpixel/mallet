import test.helpers as helpers
import nose.tools as nt

import test.fixtures.alignment_fixtures as fixtures

import mallet.sequence as seq
import mallet.output.mallet_writer as mallet_writer

tmp_output_filename = "/tmp/output.mallet"

class TestSequenceParser(object):

    def subject(self, alignments = None, output_filename = None):
        if alignments is None: alignments = fixtures.alignments()
        if output_filename is None: output_filename = tmp_output_filename
        mallet_writer.write(alignments, output_filename)

    def assert_output(self, output):
        helpers.assert_file_contents("test/files/{}".format(output), tmp_output_filename)

    def assert_gzipped_output(self, output):
        helpers.assert_gzipped_file_contents("test/files/{}".format(output), tmp_output_filename + ".gz")

    def test_empty(self):
        self.subject([])
        self.assert_output("empty")

    def test_sample(self):
        self.subject()
        self.assert_output("mallet/sample.mallet")

    def test_with_none_states(self):
        self.subject(fixtures.none_state_alignments())
        self.assert_output("mallet/none_states.mallet")

    def test_with_long_alignments(self):
        self.subject(fixtures.long_alignments())
        self.assert_output("mallet/long_alignments.mallet")

    def test_with_none_scores(self):
        self.subject(fixtures.none_score_alignments())
        self.assert_output("mallet/none_score_alignments.mallet")

    def test_with_gz_filename(self):
        tmp_file = tmp_output_filename + ".gz"
        self.subject(fixtures.alignments(), tmp_file)
        self.assert_gzipped_output("mallet/sample.mallet")

