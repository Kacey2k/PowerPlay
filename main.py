# todo:
# initialize GUI
# initialize Settings
# Check app state (configured / not configured)
# likely application log

import tkinter as tk

def main():
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="icon.png"))
    root.title("PowerPlay")
    root.geometry("1500x700")
    root.resizable(False, False)
    root.configure(bg="black")
    root.attributes("-alpha", 1) # this is actually cool, maybe have this be an optional slider in the future?
    main_window = tk.Frame(root)

    main_window.pack()

    root.mainloop()


if __name__ == "__main__":
    main()