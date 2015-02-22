import test.helpers as helpers
import nose.tools as nt

import mallet.hmm as hmm
import mallet.input.tgf_parser as tgf

import test.fixtures.hmm_fixtures as fixtures

class TestTGFParser(object):

    def subject(self, filename = "simple.tgf"):
        return tgf.parse("test/files/tgf/{}".format(filename))

    def test_it_returns_a_hmm(self):
        helpers.assert_type(self.subject(), hmm.HMM)

    def test_simple_tgf(self):
        nt.assert_equals(self.subject(), fixtures.hmm())

    def test_ignores_comments_tgf(self):
        nt.assert_equals(self.subject("simple_with_comments.tgf"), fixtures.hmm())

    def test_invalid_tgf_file(self):
        nt.assert_raises(ValueError, self.subject, "invalid.tgf")
