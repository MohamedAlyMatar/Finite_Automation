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

def cfg_to_pda(cfg):
    variables, terminals, start_variable, production_rules = cfg

    # Step 1: Create a new PDA with a single state q
    state = 'q'
    start_state = state
    start_symbol = '$'
    accept_states = {state}
    transitions = {}

    # Step 2: Add transitions for each production rule in the CFG
    for variable, rules in production_rules.items():
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
    transition_value = (state, start_variable + start_symbol)
    transitions.setdefault(transition_key, []).append(transition_value)

    pda = PDA(transitions, start_state, start_symbol, accept_states)
    return pda

# Example usage
cfg_variables = {'S','B'}
cfg_terminals = {'a', 'b','c'}
cfg_start_variable = 'S'
cfg_production_rules = {
    'S': ['aBc', 'ab'],
    'B': ['SB', 'e']
}

cfg = (cfg_variables, cfg_terminals, cfg_start_variable, cfg_production_rules)
pda = cfg_to_pda(cfg)

print("cfg_variables", type(cfg_variables))
print("cfg_terminals", type(cfg_terminals))
print("cfg_start_variable", type(cfg_start_variable))
print("cfg_production_rules", type(cfg_production_rules))
print(cfg_production_rules)

print(pda)