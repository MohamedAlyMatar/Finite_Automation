import tkinter as tk
from tkinter import messagebox
from classes_def import *
from draw import *

def convert_user_input():
    # Get the input from the GUI
    nfa_states = nfa_states_entry.get().split(',')
    nfa_alphabet = nfa_alphabet_entry.get().split(',')

    # initialize an empty dictionary for the nfa transitions
    nfa_transitions = {}

    for line in nfa_transitions_text.get('1.0', tk.END).split('\n'):
        if line:
            parts = line.split(',')
            # check if the user entered the transitions correctly
            # they must be at least 3 parts
            if len(parts) < 3:
                messagebox.showerror("Input Error", "Invalid input format for NFA transitions")
                return
            
            # divide the parts into the three main definitions we will work with
            # the star before the next_states means that it take more than one argument
            state, input, *next_states = parts

            for inp in input:
                if inp == 'e':
                    input = None
            
            # if the state is not found in the transitions add and initialize it in the dictionary
            if state not in nfa_transitions:
                nfa_transitions[state] = {}
            
            # now for each state's input we set the next states for it
            nfa_transitions[state][input] = set(next_states)

    # get the start and accept states from the user
    nfa_start_state = nfa_start_state_entry.get()
    nfa_accept_states = set(nfa_accept_states_entry.get().split(','))

    # assign everything we converted to a NFA class
    nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accept_states)
    # Convert the NFA to DFA
    dfa = nfa_to_dfa(nfa)

    # Update the GUI with the DFA states
    dfa_states_text.delete(1.0, tk.END)
    dfa_states_text.insert(tk.END, str(dfa.states))

    dfa_trans_text.delete(1.0, tk.END)
    dfa_trans_text.insert(tk.END, str(dfa.transitions))

    # print(dfa.transitions)
    # returning the nfa is not doing anything except that we will need it for graphing
    return nfa

def draw__nfa():
    nfa = convert_user_input()
    print('NFA transitions:\n', nfa.transitions)
    nfa_to_dot(nfa)

def draw__dfa():
    nfa = convert_user_input()
    dfa = nfa_to_dfa(nfa)
    print('DFA transitions:\n', dfa.transitions)
    dfa_to_dot(dfa)

# -------------------- Code for GUI -------------------- #

# Create the main window
root = tk.Tk()
root.title("NFA to DFA Converter")

# Create the input labels and entries
nfa_states_label = tk.Label(root, text="NFA States:")
nfa_states_label.grid(row=0, column=0)
nfa_states_entry = tk.Entry(root)
nfa_states_entry.grid(row=0, column=1)

nfa_alphabet_label = tk.Label(root, text="Alphabet:")
nfa_alphabet_label.grid(row=1, column=0)
nfa_alphabet_entry = tk.Entry(root)
nfa_alphabet_entry.grid(row=1, column=1)

nfa_transitions_label = tk.Label(root, text="Transitions (state,symbol,next_states):")
nfa_transitions_label.grid(row=2, column=0)
nfa_transitions_text = tk.Text(root, height=10)
nfa_transitions_text.grid(row=2, column=1)

nfa_start_state_label = tk.Label(root, text="Start State:")
nfa_start_state_label.grid(row=3, column=0)
nfa_start_state_entry = tk.Entry(root)
nfa_start_state_entry.grid(row=3, column=1)

nfa_accept_states_label = tk.Label(root, text="Accept States (comma-separated):")
nfa_accept_states_label.grid(row=4, column=0)
nfa_accept_states_entry = tk.Entry(root)
nfa_accept_states_entry.grid(row=4, column=1)

# Create the button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_user_input)
convert_button.grid(row=5, column=0)

  
convert_button = tk.Button(root, text="Draw NFA", command=draw__nfa)
convert_button.grid(row=25, column=0)

convert_button = tk.Button(root, text="Draw DFA", command=draw__dfa)
convert_button.grid(row=25, column=1)

# Create the output label and text box for displaying the resulting DFA states
dfa_states_label = tk.Label(root, text="DFA States:")
dfa_states_label.grid(row=6, column=0)
dfa_states_text = tk.Text(root, height=10)
dfa_states_text.grid(row=6, column=1)

# Create the output label and text box for displaying the resulting DFA states
dfa_trans_label = tk.Label(root, text="DFA Transitions:")
dfa_trans_label.grid(row=12, column=0)
dfa_trans_text = tk.Text(root, height=10)
dfa_trans_text.grid(row=12, column=1)

root.mainloop()