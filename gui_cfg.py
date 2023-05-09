import tkinter as tk
from tkinter import ttk
from classes_def_cfg import *

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

root = tk.Tk()
root.resizable(0,0)
root.title("CFG to PDA")

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
title = ttk.Label(main_frame, text="Welcome!", font=('TkDefaultFont', 16))
title.grid(row=0, column=0)

# create the input label and box
input_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
input_frame.grid(row=1, column=0, padx=10, pady=10)
input_label = ttk.Label(input_frame, text="Enter CFG:")
input_label.grid(row=0, column=0)
input_box = tk.Text(input_frame, height=7, width=70)
input_box.grid(row=1, column=0)

# create the output label and box
output_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
output_frame.grid(row=3, column=0, padx=10, pady=10)
output_label = ttk.Label(output_frame, text="PDA Transition Table:")
output_label.grid(row=0, column=0)
output_box = tk.Text(output_frame, height=17, width=70)
output_box.grid(row=1, column=0)

# create the generate button
# generate_button = ttk.Button(root, text="Generate Table", command=generate_table())
# generate_button = ttk.Button(root, text="Generate Table", command=lambda: output_box.insert(tk.END, generate_pda_from_cfg().generate_table()))
generate_button = ttk.Button(main_frame, text="Generate Table", command=convert_user_cfg)
generate_button.grid(row=2,column=0)

# start the main loop
root.mainloop()