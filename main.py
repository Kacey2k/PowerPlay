import sys
import uuid
from PyQt5.QtWidgets import QApplication

from config import check_config, cfg_app_state
from configure_window import configure_window
from main_window import MainWindow
from src.modules.debug import log_message

X_RUNTIME_ID = None

def generate_runtime_id():
    global X_RUNTIME_ID
    X_RUNTIME_ID = uuid.uuid4().int
    runtime_debug_string = f"[Main] | [Info] A New Runtime ID has been generated. ID: {X_RUNTIME_ID}"
    log_message(runtime_debug_string)

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
    generate_runtime_id()
    main()