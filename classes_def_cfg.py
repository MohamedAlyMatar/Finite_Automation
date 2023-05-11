# ------------------- define classes for CFG and PDA with their formal definitions ------------------- #

class CFG:
    def __init__(self, non_terminals, terminals, productions, start_var):
        self.nonterminals = non_terminals
        self.terminals = terminals
        self.production = productions
        self.start_var = start_var


class PDA:
    def __init__(self, start_state, start_symbol, accept_states, transitions):
        self.start_state = start_state
        self.start_symbol = start_symbol
        self.accept_states = accept_states
        self.transitions = transitions

    def __str__(self):
        output = "Transition Table Rules:\nδ(current state, char read, char pop) = (new state, char push)\ne stands for epsilon\n\n"
        i = 0
        for key, values in self.transitions.items():
            for value in values:
                i += 1
                output += f"Rule {i}: δ({key[0]}, {key[1]}, {key[2]}) = ({value[0]}, {value[1]})\n"
        return output
    

# ------------------- main function that converts the cfg to pda transition rules ------------------- #

def cfg_to_pda(cfg):
    non_terminals, terminals, productions, start_var = cfg

    # Define the PDA
    start_stack_symbol = '$'
    init_state = 'qO'
    start_state = 'qS'
    loop_state = 'qL'
    accept_state = 'qf'
    transitions = {}
    # state_count = 0

    # --------------------------------------------------------------------------- #

    # Add the initial state
    transition_key = (init_state, 'e', 'e')
    transition_value = (start_state, start_stack_symbol)

    # search for transition key in transitions 
    # if not found create it with an empty value
    # if found append the transition
    transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    # Add the start state
    transition_key = (start_state, 'e', 'e')
    transition_value = (loop_state, start_var)

    # search for transition key in transitions 
    # if not found create it with an empty value
    # if found append the transition
    transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    # Add terminal transitions on the loop state
    for terminal in terminals:
        # state = 'q' + str(state_count)
        # state_count += 1
        transition_key = (loop_state, terminal, terminal)
        transition_value = (loop_state, 'e')

        # search for transition key in transitions 
        # if not found create it with an empty value
        # if found append the transition
        transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    states_counter = 0
    for variable, rules in productions.items():
        for rule in rules:
            current_state = loop_state
            loop_var = variable
            ch = -1
            for i in range(1, len(rule)):
                states_counter += 1
                next_state = "q" + str(states_counter)
            
                transition_key = (current_state, 'e', loop_var)
                transition_value = (next_state, rule[ch])
                transitions.setdefault(transition_key, []).append(transition_value)
                current_state = next_state
                loop_var = 'e'
                ch = ch -1

            transition_key = (current_state, 'e', 'e')
            transition_value = (loop_state, rule[ch])
            transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    # Add a final state qf to accept the input string
    transition_key = (loop_state, 'e', start_stack_symbol)
    transition_value = (accept_state, 'e')

    # search for transition key in transitions 
    # if not found create it with an empty value
    # if found append the transition
    transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    pda = PDA(start_state, start_stack_symbol, accept_state, transitions)
    return pda


