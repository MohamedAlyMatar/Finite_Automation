# ------------------- define classes for NFA and DFA with their formal definitions ------------------- #

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states


class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

# here we get all the epsilon transitions that could happen
def epsilon_closure(nfa, given_states):
    # initialize the closure and stack with the given states to begin working
    closure = set(given_states)
    rem_states = list(given_states)

    while rem_states:
        # assign the current state to one of the stack states by poping
        current_state = rem_states.pop()

        # if the current state is found in the NFA transitions 
        # and it's coresponding transition input is NONE
        if current_state in nfa.transitions and None in nfa.transitions[current_state]:
            # then for every next transitions 
            for epsilon_state in nfa.transitions[current_state][None]:
                # check if it's in the set of closure or not
                if epsilon_state not in closure:
                    # if not then add it to the closure 
                    # and to the stack to check on it
                    closure.add(epsilon_state)
                    rem_states.append(epsilon_state)
    
    # then return the closure
    return frozenset(closure)


def move(nfa, states, input):
    # initialize an empty set to store the set of transition states
    move_states = set()

    # for each state
    for state in states:
        # check if the state is found in the NFA transition 
        # and it's input transition is found with the state
        if state in nfa.transitions and input in nfa.transitions[state]:
            # then add them to the move states
            move_states.update(nfa.transitions[state][input])
    
    # then return the epsilon clousure to make to get all the set states 
    return epsilon_closure(nfa, move_states)



# ------------------- function to clean and adjust the DFA formal definition for the fm graph ------------------- #

def clean_frozenset(dfa):
    for state in dfa.states:
        if isinstance(state, frozenset):
            dfa.states.remove(state)
            dfa.states.add(str(state)[11:-2].replace("'", "").replace(" ", "").replace(",", ""))
    
    for a_state in dfa.accept_states:
        if isinstance(a_state, frozenset):
            dfa.accept_states.remove(a_state)
            dfa.accept_states.add(str(a_state)[11:-2].replace("'", "").replace(" ", "").replace(",", ""))

    new_keys = []
    new_dict = {}
    c = 0
    for k in dfa.transitions.keys():
        new_keys.append(str(k)[11:-2].replace("'", "").replace(" ", "").replace(",", ""))
        new_dict[new_keys[c]] = dfa.transitions[k]
        c += 1
    dfa.transitions = new_dict

    for next in dfa.transitions:
        for key in dfa.transitions[next]:
            if isinstance(dfa.transitions[next][key], frozenset):
                dfa.transitions[next][key] = str(dfa.transitions[next][key])[11:-2].replace("'", "").replace(" ", "").replace(",", "")



# ------------------- function to convert the NFA to DFA ------------------- #

def nfa_to_dfa(nfa):
    start_state = epsilon_closure(nfa, {nfa.start_state})
    dfa_states = {start_state}
    dfa_transitions = {}
    dfa_accept_states = set()
    rem_states = [start_state]

    while rem_states:
        current_state = rem_states.pop()
        
        for input in nfa.alphabet:
            next_state = move(nfa, current_state, input)

            # check if next_state is NOT empty
            if len(next_state) > 0:

                # if the next state is a new created one 
                # then add it to the dfa states 
                # and append to the stack to work on it too
                if next_state not in dfa_states:
                    dfa_states.add(next_state)
                    rem_states.append(next_state)

                # if the current state is a new dfa transition
                # then initialize it to its corresponding dfa transition 
                if current_state not in dfa_transitions:
                    dfa_transitions[current_state] = {}

                # now set everything up with the next states we got
                dfa_transitions[current_state][input] = next_state

        # if my current state has a common state with the accept states 
        # then it's also an accept state
        if len(current_state.intersection(nfa.accept_states)) > 0:
            dfa_accept_states.add(current_state)

        dfa = DFA(dfa_states, nfa.alphabet, dfa_transitions, start_state, dfa_accept_states)
        clean_frozenset(dfa)
    return dfa
