import tkinter as tk
from tkinter import ttk

def my_custom_theme():
    main_window = tk.Tk()
    main_window.resizable(0,0)
    dark_style = ttk.Style()
    icon = tk.PhotoImage(file="ASU_logo.png")
    main_window.iconphoto(True, icon)

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

    return main_window