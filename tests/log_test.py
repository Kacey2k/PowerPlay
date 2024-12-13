import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root)

from config import cfg_user_directory

console_log = cfg_user_directory + "/tf/console.log"

LOG_PRESENT = False
LOG_LINES = 0

def check_log():
    global LOG_PRESENT
    if os.path.exists(console_log):
        LOG_PRESENT = True
        print("[Logger] | [Info] console.log found.")
    else:
        LOG_PRESENT = False
        print("[Logger] | [Warning] console.log not found!")

check_log()