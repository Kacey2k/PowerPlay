import tkinter as tk
import configparser
from tkinter import filedialog


def configure_window():
    root = tk.Tk()
    root.title("PowerPlay")
    root.geometry("600x300")
    root.configure(bg="#1f1f1f")

    # Port Field (only accepts numbers)
    def validate_input(input):
        if input.isdigit():
            return True
        else:
            return False

    vcmd = (root.register(validate_input), '%P')
    input_RCONPort_label = tk.Label(root, text="RCON Port", bg="black", fg="white", font=("Arial", 12))
    input_RCONPort_label.pack(pady=(10, 0))
    input_RCONPort = tk.Entry(root, width=50, bg="#333333", fg="white", borderwidth=0, font=("Arial", 12), validate="key", validatecommand=vcmd)
    input_RCONPort.pack(pady=(0, 10))

    # Password Field
    input_RCONPassword_label = tk.Label(root, text="RCON Password", bg="black", fg="white", font=("Arial", 12))
    input_RCONPassword_label.pack(pady=(10, 0))
    input_RCONPassword = tk.Entry(root, width=50, bg="#333333", fg="white", borderwidth=0, font=("Arial", 12))
    input_RCONPassword.pack(pady=(0, 10))

    # TF Directory Field
    input_TFDirectory_label = tk.Label(root, text="TF Directory", bg="black", fg="white", font=("Arial", 12))
    input_TFDirectory_label.pack(pady=(10, 0))
    input_TFDirectory_frame = tk.Frame(root, bg="#1f1f1f")
    input_TFDirectory_frame.pack(pady=(0, 10))
    input_TFDirectory = tk.Entry(input_TFDirectory_frame, width=43, bg="#333333", fg="white", borderwidth=0, font=("Arial", 12))
    input_TFDirectory.pack(side=tk.LEFT, padx=(0, 10))

    def select_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            input_TFDirectory.delete(0, tk.END)
            input_TFDirectory.insert(0, folder_selected)

    folder_select_button = tk.Button(input_TFDirectory_frame, text="Browse", command=select_folder, bg="#555555", fg="white", borderwidth=0, font=("Arial", 12), height=1)
    folder_select_button.pack(side=tk.RIGHT)

    def submit_input():
        rcon_port = input_RCONPort.get()
        rcon_password = input_RCONPassword.get()
        tf_directory = input_TFDirectory.get()
        if rcon_port and rcon_password and tf_directory:
            print("[TEST] User input:", rcon_port, rcon_password, tf_directory)
            
            config = configparser.ConfigParser()
            config.read('settings_sample.ini')
            
            if not config.has_section('rcon'):
                config.add_section('rcon')
            if not config.has_section('user'):
                config.add_section('user')
            if not config.has_section('app'):
                config.add_section('app')
            
            config.set('rcon', 'rcon_port', rcon_port)
            config.set('rcon', 'rcon_password', rcon_password)
            config.set('user', 'directory', tf_directory)
            config.set('app', 'state', '1')
            
            with open('settings_sample.ini', 'w') as configfile:
                config.write(configfile)
                
            print("[TEST] Settings updated successfully.")
            # this is where the main script would then be called normally
        else:
            print("[TEST] Please provide all inputs.")

    submit_button = tk.Button(root, text="Submit", command=submit_input, bg="#555555", fg="white", borderwidth=0, font=("Arial", 12))
    submit_button.pack(pady=(20, 0))

    root.mainloop()

if __name__ == "__main__":
    configure_window()