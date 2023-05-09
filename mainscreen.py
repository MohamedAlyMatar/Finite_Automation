import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        
        # Create two frames to hold the two different GUIs
        self.frame1 = ttk.Frame(self)
        self.frame2 = ttk.Frame(self)
        
        # Create a menu bar with two scroll buttons to switch between the frames
        self.menu_bar = tk.Menu(self)
        self.menu_bar.add_command(label="GUI 1", command=self.show_frame1)
        self.menu_bar.add_command(label="GUI 2", command=self.show_frame2)
        self.config(menu=self.menu_bar)
        
        # Create the contents of GUI 1 and add them to frame 1
        self.label1 = ttk.Label(self.frame1, text="GUI 1")
        self.label1.pack(pady=10)
        self.button1 = ttk.Button(self.frame1, text="Button 1")
        self.button1.pack(pady=10)
        
        # Create the contents of GUI 2 and add them to frame 2
        self.label2 = ttk.Label(self.frame2, text="GUI 2")
        self.label2.pack(pady=10)
        self.button2 = ttk.Button(self.frame2, text="Button 2")
        self.button2.pack(pady=10)
        
        # Show the first frame
        self.show_frame1()
    
    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack(fill=tk.BOTH, expand=1)
    
    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack(fill=tk.BOTH, expand=1)

if __name__ == '__main__':
    app = App()
    app.mainloop()


# import tkinter as tk
# import os

# def open_gui1():
#     os.system('python gui_fm.py')

# def open_gui2():
#     os.system('python gui_cfg.py')

# root = tk.Tk()

# # Create buttons to open the two GUI files
# button1 = tk.Button(root, text="Open GUI 1", command=open_gui1)
# button1.pack()

# button2 = tk.Button(root, text="Open GUI 2", command=open_gui2)
# button2.pack()

# root.mainloop()
