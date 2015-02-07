import mallet.hmm as hmm
import mallet.state as state

# regular expressions
import re

STATUSES = ('state', 'transition', 'emission')

# TODO: Horrible code... improve!!
def parse(filename):
    """
    It processes a TGF file and returns a HMM object ready to roll.
    """
    # initialize status and status iterator
    statuses = iter(STATUSES)
    status = next(statuses)

    states = {}

    with open(filename, 'r') as tgf_file:
        for line in tgf_file:
            # match all words in each line
            columns = re.findall("[^\s]+", line.strip())

            # change of status
            if columns[0] == '#':
                status = next(statuses)
                continue
            # comments
            elif columns[0].startswith(";"):
                continue

            if status == 'state':
                id_state, long_name, short_name = (int(columns[0]), columns[1], columns[2])
                states[id_state] = state.State(id_state, long_name, short_name)
            elif status == 'transition':
                id_state, id_dst_state, probability = (int(columns[0]), int(columns[1]), float(columns[2]))
                initial_state = states[id_state]
                dst_state = states[id_dst_state]
                initial_state.transitions[dst_state] = probability
            elif status == 'emission':
                id_state, emission, probability = (int(columns[0]), columns[1], float(columns[2]))
                states[id_state].emissions[emission] = probability

    model = hmm.HMM(states)
    model.is_valid()
    return model
