import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes_def_fm import *
from draw_fm import *
from dark_style import my_dark_theme

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

root = tk.Tk()
root.resizable(0,0)
root.title("NFA to DFA Converter")


# -------------------- Custom style -------------------- #

dark_style = ttk.Style()

# Define the colors for the various elements of the theme
dark_style.theme_create("my_dark_theme", parent="alt", settings={
    ".": {
        "configure": {
            "background": "#333333",
            "foreground": "#FFFFFF",
            "selectbackground": "#505050",
            "selectforeground": "#FFFFFF"
        }
    },
    # Set the color and styling for the buttons
    # ttk.Style().map("TButton", background=[("active", "#aaa")], foreground=[("active", "#fff")])
    "TButton": {
        "map": {
            "background": [("active", "#aaa")],
            "foreground": [("active", "#fff")]
        },
        "configure": {
            "padding": 6,
            "relief": "flat",
            "background": "#f7970a",
            "foreground": "#FFFFFF"
        }
    },
    "TEntry": {
        "configure": {
            "background": "#FFFFFF",
            "foreground": "#000000"
        }
    },
    "TLabel": {
        "configure": {
            "foreground": "#f7970a"
        }
    },
})

# Set the new theme as the default
dark_style.theme_use("my_dark_theme")

# -------------------- Custom style -------------------- #


# Create a main frame to contain all the widgets
main_frame = ttk.Frame(root, padding=10)
main_frame.grid()

title = ttk.Label(main_frame, text="Welcome!")
title.grid(row=0, column=0, columnspan=3)

# Create a frame for the input section
input_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
input_frame.grid(row=1, column=0, padx=10, pady=10)

# Create the input labels and entries
nfa_states_label = ttk.Label(input_frame, text="NFA States:")
nfa_states_label.grid(row=1, column=0)
nfa_states_entry = ttk.Entry(input_frame)
nfa_states_entry.grid(row=2, column=0)

nfa_alphabet_label = ttk.Label(input_frame, text="Alphabet:")
nfa_alphabet_label.grid(row=3, column=0)
nfa_alphabet_entry = ttk.Entry(input_frame)
nfa_alphabet_entry.grid(row=4, column=0)

nfa_start_state_label = ttk.Label(input_frame, text="Start State:")
nfa_start_state_label.grid(row=5, column=0)
nfa_start_state_entry = ttk.Entry(input_frame)
nfa_start_state_entry.grid(row=6, column=0)

nfa_accept_states_label = ttk.Label(input_frame, text="Accept States (comma-separated):")
nfa_accept_states_label.grid(row=7, column=0)
nfa_accept_states_entry = ttk.Entry(input_frame)
nfa_accept_states_entry.grid(row=8, column=0)

trans_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
trans_frame.grid(row=1, column=1, padx=10, pady=10)

nfa_transitions_label = ttk.Label(trans_frame, text="Transitions (state,symbol,next_states):")
nfa_transitions_label.grid(row=2, column=0, columnspan=2)
nfa_transitions_text = tk.Text(trans_frame, height=5, width=50)
nfa_transitions_text.grid(row=3, column=0, columnspan=2)

# Create the button to trigger the conversion
convert_button = ttk.Button(trans_frame, text="Convert", command=convert_user_input)
convert_button.grid(row=10, column=0, pady=10)

# Create the button to draw the NFA
draw_nfa_button = ttk.Button(trans_frame, text="Draw NFA", command=draw__nfa)
draw_nfa_button.grid(row=10, column=1, pady=10)

# Create a frame for the output section
dfa_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
dfa_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the output labels and text boxes
dfa_states_label = ttk.Label(dfa_frame, text="DFA States:")
dfa_states_label.grid(row=1, column=0)
dfa_states_text = tk.Text(dfa_frame, height=5, width=50)
dfa_states_text.grid(row=2, column=0)

# Create the output label and text box for displaying the resulting DFA transitions
dfa_trans_label = ttk.Label(dfa_frame, text="DFA Transitions:")
dfa_trans_label.grid(row=4, column=0)
dfa_trans_text = tk.Text(dfa_frame, height=5, width=50)
dfa_trans_text.grid(row=5, column=0)

# Create the button to draw the DFA
draw_dfa_button = ttk.Button(dfa_frame, text="Draw DFA", command=draw__dfa)
draw_dfa_button.grid(row=4, column=3, padx=10)

root.mainloop()