import sys
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtGui import QIcon

from window_style import set_styles

# Modules
from src.modules.debug import debug_tab, log_message
from src.modules.tab_players import players_tab
from src.modules.tab_attributes import attributes_tab
from src.modules.tab_killfeed import killfeed_tab
from src.modules.tab_maps import maps_tab
from src.modules.tab_servers import servers_tab
from src.modules.tab_tfmail import tfmail_tab
from src.modules.tab_user import user_tab
from src.modules.tab_settings import settings_tab

# Util
# from src.util.app_control import state_check
from src.util.rcon_handler import r_debug_confirmation

config = configparser.ConfigParser()
config.read("settings.ini")
debug_visible = False
if config.has_section("app"):
    if config.has_option("app", "debug"):
        debug = config.get("app", "debug")
        if debug == "1":
            debug_visible = True
            log_message("[main_window.py: config check] Debug mode enabled!")
        else:
            debug_visible = False
    else:
        log_message("[main_window.py: config check] settings.ini missing 'debug' option")
        debug_visible = False

    # Some Notes:
    # - Each tab is a separate module in the src/modules directory
    # - Each tab is a class that inherits from QWidget
    # - Debug log is a global variable that is updated in the debug_tab function
    # - log_message is a very helpful function is used to log messages to the debug log and console
    # --- Find your logs in: data/logs/ (requires debug mode set to 1 in settings.ini)
    # - You may adjust the styling in window_style.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PowerPlay")
        self.setGeometry(100, 100, 1500, 700)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet(set_styles())

        self.central_widget.addTab(players_tab(), "Players")
        self.central_widget.addTab(attributes_tab(), "Attributes")
        self.central_widget.addTab(killfeed_tab(), "Killfeed")
        self.central_widget.addTab(maps_tab(), "Maps")
        self.central_widget.addTab(servers_tab(), "Servers")
        self.central_widget.addTab(tfmail_tab(), "TFMail")
        self.central_widget.addTab(user_tab(), "User")
        self.central_widget.addTab(settings_tab(), "Settings")

        if debug_visible:
            debug_tab(self.central_widget)

        log_message("[main_window.py] Main window initialized.")
        log_message("[main_window.py] Log for this run located in /data/logs")

        r_debug_confirmation()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
