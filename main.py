# Check app state (configured / not configured)

import os
import tkinter as tk
import configparser
from src.gui.configure_window import configure_window
from src.gui.main_window import main_window

def check_state(): # look for "state" in settings.ini
    """Checks settings.ini for state. If state is 1, we are configured. If state is 0, we are not configured."""
    if os.path.exists("settings.ini"):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        if config.has_section("app"):
            if config.has_option("app", "state"):
                state = config.get("app", "state")
                if state == "1":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
if check_state() == False:
    print("[main.py] NOT Configured")
    configure_window()
    # remove this window after running configure_window.py
else:
    main_window()
    print("[main.py] Configured")
    # remove this window after running main_window.py

def main():
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="icon.png"))
    root.title("PowerPlay")
    root.geometry("1500x700")
    root.resizable(False, False)
    root.configure(bg="#1f1f1f")
    root.attributes("-alpha", 1) # this is actually cool, maybe have this be an optional slider in the future?
    main_window = tk.Frame(root)

    main_window.pack()

    root.mainloop()


if __name__ == "__main__":
    main()