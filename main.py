import tkinter as tk
from tkinter import ttk
import os

def open_gui1():
    os.system('python gui_fm.py')

def open_gui2():
    os.system('python gui_cfg.py')

root = tk.Tk()
root.resizable(0,0)
# root.geometry('400x100')
root.title("TOOLS")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid()
title = ttk.Label(main_frame, text="Please choose what you want to do")
title.grid(row=0, column=0)

# Create buttons to open the two GUI files
button1 = tk.Button(main_frame, text="Open GUI 1", command=open_gui1)
button1.grid(row=1, column=0)

button2 = tk.Button(main_frame, text="Open GUI 2", command=open_gui2)
button2.grid(row=2, column=0)

root.mainloop()