import os
import sys
import configparser
from PyQt5.QtWidgets import QApplication # god have mercy on my soul

from configure_window import configure_window
from main_window import MainWindow
from src.modules.debug import log_message

def main():
    def check_state():
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
                    log_message("[main.py: check_state] settings.ini missing 'app' option: 'state'")
                    return False
            else:
                log_message("[main.py: check_state] settings.ini missing 'app' section")
                return False
        else:
            log_message("[main.py: check_state] settings.ini not found!")
            return False

    app = QApplication(sys.argv)

    if check_state() == False:
        log_message("[main.py: check_state] NOT Configured!")
        configure_window()
    else:
        log_message("[main.py: check_state] Configured!")
        window = MainWindow()
        window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
