import tkinter as tk
from tkinter import ttk
from tkinter import *
from dark_style import *
import os

def open_gui1():
    os.system('python gui_fm.py')

def open_gui2():
    os.system('python gui_cfg.py')


main_window = my_custom_theme()
main_window.title("TOOLS")

main_frame = ttk.Frame(main_window, padding=10)
main_frame.grid()
title1 = ttk.Label(main_frame, text="Welcome Engineers :)", font=('TkDefaultFont', 14))
title1.grid(row=0, column=0)
title2 = ttk.Label(main_frame, text="Please choose what you want to do", font=('TkDefaultFont', 12))
title2.grid(row=1, column=0)

buttons_frame = ttk.Frame(main_frame, padding=10, relief=tk.GROOVE, borderwidth=2)
buttons_frame.grid(row=2, column=0, padx=10, pady=10)

# Create buttons to open the two GUI files
button1 = ttk.Button(buttons_frame, text="NFA to DFA", command=open_gui1)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = ttk.Button(buttons_frame, text="CFG to PDA", command=open_gui2)
button2.grid(row=1, column=0, padx=10, pady=10)

main_window.mainloop()