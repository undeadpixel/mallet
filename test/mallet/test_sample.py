import test.helpers as helpers
import nose.tools as nt

import mallet.sample as sample
import mallet.hmm as hmm
import mallet.input.tgf_parser as tgf

# import some fixtures
# import test.fixtures.hmm_fixtures as fixtures

class TestSample(object):

    def subject(self, hmm, observations = 10):
        return sample.sample(hmm, observations)

    # def test_blah(self):
    #     hmm = tgf.parse("test/files/simple.tgf")
    #     nt.assert_equals(self.subject(hmm), ())

