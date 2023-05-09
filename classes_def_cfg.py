class CFG:
    def __init__(self, non_terminals, terminals, productions, start_var):
        self.nonterminals = non_terminals
        self.terminals = terminals
        self.production = productions
        self.start_var = start_var

class PDA:
    def __init__(self, transitions, start_state, start_symbol, accept_states):
        self.transitions = transitions
        self.start_state = start_state
        self.start_symbol = start_symbol
        self.accept_states = accept_states

    def __str__(self):
        output = "Transition table:\nstart state, symbol read, symbol popped --> new state, symbols pushed\n"
        for key, values in self.transitions.items():
            for value in values:
                output += f"{key[0]}, {key[1]}, {key[2]} --> {value[0]}, {value[1]}\n"
        output += f"Start state: {self.start_state}\n"
        output += f"Start symbol: {self.start_symbol}\n"
        output += f"Accept states: {self.accept_states}\n"
        return output

# class PDA:
#     def __init__(self, states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_states):
#         self.states = states
#         self.input_alphabet = input_alphabet
#         self.stack_alphabet = stack_alphabet
#         self.transitions = transitions
#         self.start_state = start_state
#         self.start_stack_symbol = start_stack_symbol
#         self.accept_states = accept_states

#     def generate_table(self):
#         table = ''
#         for state in self.states:
#             for stack_symbol in self.stack_alphabet:
#                 for input_symbol in self.input_alphabet:
#                     key = (state, input_symbol, stack_symbol)
#                     if key in self.transitions:
#                         dest_state, new_stack_symbol = self.transitions[key]
#                         table += f'{state}, {input_symbol}, {stack_symbol} -> {new_stack_symbol}:{dest_state}\n'
#                     else:
#                         table += f'{state}, {input_symbol}, {stack_symbol} -> error\n'
#                 table += '\n'
#         return table
    

def cfg_to_pda(cfg):
    non_terminals, terminals, productions, start_var = cfg

    # Step 1: Create a new PDA with a single state q
    state = 'q'
    start_state = state
    start_symbol = '$'
    accept_states = {state}
    transitions = {}

    # Step 2: Add transitions for each production rule in the CFG
    for variable, rules in productions.items():
        for rule in rules:
            transition_key = (state, 'e', variable)
            transition_value = (state, rule)
            # searches for transition key in transitions and appends the transition
            transitions.setdefault(transition_key, []).append(transition_value) 

    # Step 3: Add transitions for each terminal symbol in the CFG
    for terminal in terminals:
        transition_key = (state, terminal, terminal)
        transition_value = (state, 'e')
        transitions.setdefault(transition_key, []).append(transition_value)

    # Add a special transition for the start symbol of the PDA
    transition_key = (state, 'e', start_symbol)
    transition_value = (state, start_var + start_symbol)
    transitions.setdefault(transition_key, []).append(transition_value)

    pda = PDA(transitions, start_state, start_symbol, accept_states)
    return pda


