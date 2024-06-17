import os
import configparser
from src.gui.configure_window import configure_window
from src.gui.main_window import main_window

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
                    return False
            else:
                return False
        else:
            return False
        
    if check_state() == False:
        print("[main.py] NOT Configured")
        configure_window()
    else:
        print("[main.py] Configured")
        main_window()


if __name__ == "__main__":
    main()