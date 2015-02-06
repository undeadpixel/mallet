import mallet.test.helpers as helpers
import nose.tools as nt

import mallet.test.fixtures.sequence_fixtures as fixtures

import mallet.sequence as seq
import mallet.input.sequence_parser as sequence_parser

class TestSequenceParser(object):

    def subject(self, filename = "simple.fasta"):
        return sequence_parser.parse("test/files/{}".format(filename))

    def test_parse_list_sequences(self):
        result = self.subject()
        helpers.assert_type(result, list)
        #for elem in result:
            #helpers.assert_type(elem, seq.Sequence)

    def test_parse_simple_fasta(self):
        nt.assert_equals(self.subject(), fixtures.sequences())

    def test_parse_simple_raw(self):
        nt.assert_equals(self.subject("simple.raw"), fixtures.sequences())

