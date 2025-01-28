import sys
import os
import chardet
import re

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root)

from src.modules.debug import log_message
from src.util.app_control import _STATUS_
from src.util.rcon_handler import r_execute
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

def log_timestamped():
    """Boolean check for whether log is timestamped\n
    Example timestamp: 01/01/2025 - 12:34:56:
    """
    timestamp_pattern = re.compile(r'^\d{2}/\d{2}/\d{4} - \d{2}:\d{2}:\d{2}:')
    
    try:
        with open(LOGFILE, 'r', encoding='latin-1') as f:
            for line in f:
                if timestamp_pattern.match(line):
                    return True
            return False
    except UnicodeDecodeError as e:
        return f"Encoding Error: {e}"
    
def build_ping_config_files():
    """Builds 2 config files used for config tests.\n
    powerplayping.cfg - calls the powerplayping_reply.cfg within it after 50 ticks to produce a response in console.log
    """

    # PowerPlay Ping - Initializer cfg
    powerplayping_text = """// This file is needed for "PowerPlay" to operate normally.
echo "PowerPlay Ping Starting. . ."
exec powerplayping_reply.cfg
"""
    
    # PowerPlay Ping - Reply cfg
    powerplayping_reply_text = """// This file is needed for "PowerPlay" to operate normally.
wait 50; echo "[DEBUG] | [POWERPLAY PING]"
"""
    
    try:
        with open(cfg_user_directory + "/tf/cfg/powerplayping.cfg", 'w') as f:
            f.write(powerplayping_text)
        
        with open(cfg_user_directory + "/tf/cfg/powerplayping_reply.cfg", 'w') as f:
            f.write(powerplayping_reply_text)
    except Exception as e:
        log_message(f"Error: {e}")

def validate_configs():
    try:
        config_files = [
            cfg_user_directory + "/tf/cfg/powerplayping.cfg",
            cfg_user_directory + "/tf/cfg/powerplayping_reply.cfg"
        ]
        for file_path in config_files:
            if not os.path.exists(file_path):
                log_message(f"[LOG TOOLS] | [ERROR] Missing config file: {file_path}")
                return False
            
            with open(file_path, 'r') as f:
                content = f.read()
                if "// This file is needed for \"PowerPlay\" to operate normally." not in content:
                    log_message(f"[LOG TOOLS] | [ERROR] Config file is missing required content: {file_path}")
                    return False
        
        log_message("[LOG TOOLS] | [INFO] Config files validated successfully.")
        return True
    except Exception as e:
        log_message(f"[LOG TOOLS] | [ERROR] Failed to validate config files: {e}")
        return False


    
def log_ping():
    """Issues a ping to the console.log file using RCON"""
    try:
        r_execute("exec powerplayping.cfg")
    except Exception as e:
        log_message(f"Error: {e}")
    
if __name__ == "__main__":
    validate_configs()