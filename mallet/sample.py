import random

import hmm as h_mm
import state, sequence

# NOTE: This function can't be tested, it is completely random :(

def sample(hmm, observations):
    """
    Samples a finite number of times (observations) the given HMM. returns two sequences: State path and Emission sequence.
    """
    random.seed() # force reseeding

    state_path = seq.Sequence("State path", "")
    emission_sequence = seq.Sequence("Emission sequence", "")

    current_state = hmm.begin_state()
    for i in range(observations):
        current_state = current_state.sample_transition()
        # TODO: What if we reach END before time
        state_path.append(current_state.short_name)
        emission_sequence.append(current_state.sample_emission())

    return (state_path, emission_sequence)
