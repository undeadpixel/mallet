import mallet.hmm as h_mm
import mallet.state as state

# emissions

def emissions():
    return [
        {'A': 0.25, 'B': 0.25, 'C': 0.5},
        {'A': 0.55, 'B': 0.15, 'C': 0.3},
        {'A': 0.675, 'B': 0.20, 'C': 0.125},
        {'B': 0.5, 'C': 0.5}
        ]

def invalid_emissions():
    return [
        {'A': 0.5, 'B': 0.25, 'C': 0.10}
        ]

# states

def state_params():
    emissions_list = emissions()
    return [
        (1, 'Begin', 'BEGIN', {}),
        (2, 'State1', 'S', emissions_list[0]),
        (3, 'State2', 'T', emissions_list[1]),
        (4, 'State3', 'U', emissions_list[2]),
        (5, 'End', 'END', {}),
        ]

def states():
    state_param_list = state_params()
    return dict((params[0], state.State(*params)) for params in state_param_list)

# transitions

def transitions():
    state_list = states()
    return {
        1: {
            state_list[2]: 1.0
            },
        2: {
            state_list[2]: 0.5,
            state_list[3]: 0.5
            },
        3: {
            state_list[3]: 0.75,
            state_list[4]: 0.25
            },
        4: {
            state_list[4]: 0.15,
            state_list[5]: 0.85
            },
        5: {}
        }


def states_with_transitions():
    states_with_transitions = states()
    transition_list = transitions()
    for name, state in states_with_transitions.iteritems():
        state.transitions = transition_list[state.id_num]
    return states_with_transitions

def hmm():
    return h_mm.HMM(states_with_transitions())
