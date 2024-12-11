import sys
import os
import configparser
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QFrame
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

from src.modules.debug import log_message
from main_window import MainWindow
from config import check_config

# Some Notes:
# - This is the configuration window that appears when PowerPlay is not yet configured
# - It allows the user to input their preferred RCON Port, RCON Password, and TF Directory (Reasoning being that we want to avoid conflicts with other projects)
# - TF Directory is required for console.log parsing
# - Currently, it saves the configuration to settings_sample.ini, which is a temporary template for settings.ini

# To Do:
# - SteamID field
# - Language field
# - Debug field
# - Help button

class ConfigureWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PowerPlay")
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: #1f1f1f;")

        layout = QVBoxLayout()
        # To Do: Add header maybe

        self.input_RCONPort_label = QLabel("RCON Port")
        self.input_RCONPort_label.setStyleSheet("color: white; font: 12pt Arial;")
        layout.addWidget(self.input_RCONPort_label)

        self.input_RCONPort = QLineEdit()
        self.input_RCONPort.setStyleSheet("background-color: #333333; color: white; font: 12pt Arial;")
        self.input_RCONPort.setValidator(QIntValidator())
        layout.addWidget(self.input_RCONPort)

        self.input_RCONPassword_label = QLabel("RCON Password")
        self.input_RCONPassword_label.setStyleSheet("color: white; font: 12pt Arial;")
        layout.addWidget(self.input_RCONPassword_label)

        self.input_RCONPassword = QLineEdit()
        self.input_RCONPassword.setStyleSheet("background-color: #333333; color: white; font: 12pt Arial;")
        layout.addWidget(self.input_RCONPassword)

        self.input_TFDirectory_label = QLabel("TF2 Directory")
        self.input_TFDirectory_label.setStyleSheet("color: white; font: 12pt Arial;")
        layout.addWidget(self.input_TFDirectory_label)

        self.input_TFDirectory_frame = QFrame()
        dir_layout = QVBoxLayout()
        self.input_TFDirectory_frame.setLayout(dir_layout)
        self.input_TFDirectory_frame.setStyleSheet("background-color: #1f1f1f;")
        layout.addWidget(self.input_TFDirectory_frame)

        self.input_TFDirectory = QLineEdit()
        self.input_TFDirectory.setStyleSheet("background-color: #333333; color: white; font: 12pt Arial;")
        dir_layout.addWidget(self.input_TFDirectory)

        self.folder_select_button = QPushButton("Browse")
        self.folder_select_button.setStyleSheet("background-color: #555555; color: white; font: 12pt Arial;")
        self.folder_select_button.clicked.connect(self.select_folder)
        dir_layout.addWidget(self.folder_select_button)

        self.directory_error_label = QLabel("")
        self.directory_error_label.setStyleSheet("color: red; font: 10pt Arial;")
        self.directory_error_label.setHidden(True)
        dir_layout.addWidget(self.directory_error_label)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: #555555; color: white; font: 12pt Arial;")
        self.submit_button.clicked.connect(self.launch_main_window)
        self.submit_button.setEnabled(False)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Team Fortress 2 Directory")
        if folder_selected:
            if self.validate_tf2_directory(folder_selected):
                self.input_TFDirectory.setText(folder_selected)
                self.directory_error_label.setHidden(True)
                self.submit_button.setEnabled(True)
            else:
                self.input_TFDirectory.setText("")
                self.directory_error_label.setText("**Please select your ''Team Fortress 2'' folder. Usually located in ''steamapps/common''**")
                self.directory_error_label.setHidden(False)
                self.submit_button.setEnabled(False)

    def validate_tf2_directory(self, directory):
        return os.path.basename(directory) == "Team Fortress 2"

    def submit_input(self):
        rcon_port = self.input_RCONPort.text()
        rcon_password = self.input_RCONPassword.text()
        tf_directory = self.input_TFDirectory.text()
        if rcon_port and rcon_password and tf_directory:
            submitted_info = f"[Configuration Window - Input Submission] | RCON Port: {rcon_port}, RCON Password: {rcon_password}, TF Directory: {tf_directory}"
            log_message(submitted_info)
            
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
                
            log_message("[Configure Window] | [Info] Configuration updated!")
            check_config()
            return True
        else:
            log_message("[Configure Window] | [Error] Please provide all inputs!")
            return False

    def launch_main_window(self):
        if self.submit_input():
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()

def configure_window():
    app = QApplication(sys.argv)
    window = ConfigureWindow()
    window.show()
    sys.exit(app.exec())
