from tkinter import ttk

def my_dark_theme():
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

    return dark_style