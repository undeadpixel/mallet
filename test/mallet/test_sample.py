import test.helpers as helpers
import nose.tools as nt

import mallet.sample as sample

# import some fixtures
import test.fixtures.hmm_fixtures as fixtures

class TestSample(object):

    def subject(self, hmm, observations = 10):
        return sample.sample(hmm, observations)

    # TODO: add random control
    # def test_blah(self):
    #     nt.assert_equals(self.subject(fixtures.hmm()), ())

