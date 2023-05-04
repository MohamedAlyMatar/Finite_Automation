from graphviz import *
import matplotlib.pyplot as plt
import io

def nfa_to_dot(fm):
    # build a string representing the transitions
    transitions = ''
    for state, edges in fm.transitions.items():
        for input, next_states in edges.items():
            for next_state in next_states:
                transitions += f'{state} -> {next_state} [label="{input}"];\n'
    
    # build the dot script with the transitions and accept states
    dot_script = f'''
    digraph finite_state_machine {{
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        rankdir=LR;
        node [shape = doublecircle]; {" ".join(str(state) for state in fm.accept_states)};
        node [shape = circle];
        {transitions}
    }}
    '''
    # print("Dot script:\n", dot_script)
    graph = Source(dot_script)
    png_bytes = graph.pipe(format='png')

    img = plt.imread(io.BytesIO(png_bytes))
    plt.imshow(img)
    plt.show()


def dfa_to_dot(dfa):
    # build a string representing the transitions
    transitions = ''

    for state in dfa.states:
        if state in dfa.transitions.keys():
            for input in dfa.alphabet:
                if input in dfa.transitions[state]:
                    next_state = dfa.transitions[state][input]
                    transitions += f'{state} -> {next_state} [label="{input}"];\n'
                else:
                    print(f"No transition for input '{input}' from state '{state}'")
        else:
            print(f"No transitions from state '{state}'")

    # build the dot script with the transitions and accept states
    dot_script = f'''
    digraph finite_state_machine {{
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        rankdir=LR;
        node [shape = doublecircle]; {" ".join(str(state) for state in dfa.accept_states)};
        node [shape = circle];
        {transitions}
    }}
    '''
    # print("Dot script:\n", dot_script)
    graph = Source(dot_script)
    png_bytes = graph.pipe(format='png')

    img = plt.imread(io.BytesIO(png_bytes))
    plt.imshow(img)
    plt.show()
