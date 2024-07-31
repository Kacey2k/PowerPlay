import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import rcon
from rcon.source import Client

rcon_ip = "127.0.0.1"
rcon_port = 27015
rcon_password = "your_rcon_password"

class Terminal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PowerPlay Testing Terminal")
        self.setGeometry(100, 100, 1000, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.command_entry = QLineEdit()
        self.command_entry.setPlaceholderText("Enter Command")
        self.command_entry.returnPressed.connect(self.send_command)
        self.layout.addWidget(self.command_entry)

        self.response_display = QTextEdit()
        self.response_display.setReadOnly(True)
        self.layout.addWidget(self.response_display)

    def send_command(self):
        command = self.command_entry.text()
        self.command_entry.clear()

        try:
            with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
                response = client.run(command)
                self.response_display.append(f"Command sent: {command}")
                self.response_display.append(f"Response: {response}")
        except Exception as e:
            self.response_display.append(f"Failed to execute command '{command}': {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Terminal()
    window.show()
    sys.exit(app.exec_())