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
        output = "Transition Table Rules:\nstart state, symbol read, symbol popped --> new state, symbols pushed\n"
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
    state = 'q'
    start_state = start_var
    start_stack_symbol = 'z0'
    accept_states = {'qf'}
    transitions = {}
    # state_count = 0

    # --------------------------------------------------------------------------- #

    # Add transitions for each rule
    for variable, rules in productions.items():
        for rule in rules:
            # state = 'q' + str(state_count)
            # state_count += 1
            transition_key = (state, 'e', variable)
            transition_value = (state, rule)
            
            # search for transition key in transitions 
            # if not found create it with an empty value
            # if found append the transition
            transitions.setdefault(transition_key, []).append(transition_value)

            # Add an epsilon transition back to the start state
            # transition_key = (state, 'e', 'e')
            # transition_value = (start_state, 'e')
            # transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    # Add transitions for each terminal symbol
    for terminal in terminals:
        # state = 'q' + str(state_count)
        # state_count += 1
        transition_key = (state, terminal, terminal)
        transition_value = (state, 'e')

        # search for transition key in transitions 
        # if not found create it with an empty value
        # if found append the transition
        transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    # Add a special transition for the start symbol of the PDA
    # to allow the PDA to start with an empty stack

    transition_key = (state, 'e', start_stack_symbol)
    transition_value = (state, 'e')
    # transition_value = (state, start_var + start_stack_symbol)

    # search for transition key in transitions 
    # if not found create it with an empty value
    # if found append the transition
    transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    # Add a final state qf to accept the input string
    # final_state = 'qf'
    # transition_key = (start_state, 'e', 'e')
    # transition_value = (final_state, 'e')

    # search for transition key in transitions 
    # if not found create it with an empty value
    # if found append the transition
    # transitions.setdefault(transition_key, []).append(transition_value)

    # --------------------------------------------------------------------------- #

    pda = PDA(start_state, start_stack_symbol, accept_states, transitions)
    return pda


