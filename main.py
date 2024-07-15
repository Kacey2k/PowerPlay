import sys
from PyQt5.QtWidgets import QApplication

from config import check_config, cfg_app_state
from configure_window import configure_window
from main_window import MainWindow
from src.modules.debug import log_message

def main():
    check_config()

    app = QApplication(sys.argv)

    if cfg_app_state == 0:
        log_message("[Main] | [Info] NOT Configured!")
        configure_window()
    else:
        log_message("[Main] | [Info] Configured!")
        window = MainWindow()
        window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()