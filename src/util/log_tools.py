import sys
import os
import chardet

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root)

from src.modules.debug import log_message
from src.util.app_control import _STATUS_
from config import check_config, cfg_user_directory

LOGFILE = cfg_user_directory + "/tf/console.log"

def log_exists():
    check_config()
    if os.path.exists(LOGFILE):
        log_message("[LOG TOOLS] | [INFO] Log file exists!")
        return True
    else:
        log_message("[LOG TOOLS] | [WARNING] Log file does not exist!")
        return False

def find_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(10000)
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']

    final_encoding = log_message(f"[LOG TOOLS] | [INFO] Detected encoding: {encoding} (confidence: {confidence:.2f})")

    return final_encoding

def logging_ready():
    if _STATUS_ <= 0:
        log_message("[LOG TOOLS] | [WARNING] Console Logging is idle.")
        return False
    else:
        log_message("[LOG TOOLS] | [INFO] Console Logging is active.")
        return True

if __name__ == "__main__":
    find_encoding(LOGFILE)