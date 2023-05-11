import tkinter as tk
from tkinter import ttk
from classes_def_cfg import *
from tkinter import *
from dark_style import *


def convert_user_cfg():
    # cfg = CFG
    text = input_box.get("1.0", "end")
    nonterminals = set()
    terminals = set()
    # rules = []
    rules_dic = {}
    start_var = ''

    # Split the CFG into the list of productions
    productions = text.split('\n')
    start_var = text[0]
    for production in productions:
        if production:
            for sym in production:
                if sym.islower() and sym != 'e':
                    terminals.add(sym)
                elif sym.isnumeric():
                    terminals.add(sym)
                elif sym.isupper():
                    nonterminals.add(sym)
            print(production)
            lhs, rhs = production.strip().replace(' ','').split('->')
            rules_dic[lhs] = rhs.strip().replace(' ','').split('|')
            # rules.append((lhs, rhs.strip().split('|')))

    cfg = (nonterminals, terminals, rules_dic, start_var)
    result = cfg_to_pda(cfg)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, str(result))

# -------------------- Code for GUI -------------------- #

root = my_custom_theme()
root.title("CFG to PDA")

# Create a main frame to contain all the widgets
main_frame = ttk.Frame(root, padding=10)
main_frame.grid()
title = ttk.Label(main_frame, text="Welcome!", font=('TkDefaultFont', 16))
title.grid(row=0, column=0)

# create the input label and box
input_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
input_frame.grid(row=1, column=0, padx=10, pady=10)
input_label = ttk.Label(input_frame, text="Enter CFG:\nstart variable -> variables/terminals | variables/terminals\nuse 'e' for epsilon")
input_label.grid(row=0, column=0)
input_box = tk.Text(input_frame, height=5, width=70)
input_box.grid(row=1, column=0)

# create the output label and box
output_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
output_frame.grid(row=3, column=0, padx=10, pady=10)
output_label = ttk.Label(output_frame, text="PDA Transition Table Rules:")
output_label.grid(row=0, column=0)
output_box = tk.Text(output_frame, height=20, width=70)
output_box.grid(row=1, column=0)

# create the generate button
generate_button = ttk.Button(main_frame, text="Generate Rules", command=convert_user_cfg)
generate_button.grid(row=2,column=0)

# start the main loop
root.mainloop()