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

def search_string(string):
    """Test script for finding text in console log."""
    if not log_exists():
        return []
    
    matches = []
    try:
        escaped_pattern = re.escape(string) 
        regex = re.compile(escaped_pattern)  

        with open(LOGFILE, 'r', encoding='latin-1') as f:
            for line_number, line in enumerate(f, start=1):
                if regex.search(line):
                    matches.append((line_number, line.strip()))

        log_message(f"[LOG TOOLS -> SEARCH STRING] | [INFO] Found matching lines at {', '.join(str(num) for num, _ in matches)}. Totalling in {len(matches)} matches of '{string}'")
    except Exception as e:
        log_message(f"[LOG TOOLS -> SEARCH STRING] | [ERROR] Failed to search: {e}")
    
    return matches

def search_regex(pattern):
    """Test script for validating regex patterns in console log."""
    if not log_exists():
        return []
    
    matches = []
    try:
        regex = re.compile(pattern)

        with open(LOGFILE, 'r', encoding='latin-1') as f:
            for line_number, line in enumerate(f, start=1):
                if regex.search(line):
                    matches.append((line_number, line.strip()))

        log_message(f"[LOG TOOLS -> SEARCH REGEX] | [INFO] Found matching lines at {', '.join(str(num) for num, _ in matches)}. Totalling in {len(matches)} matches of '{pattern}'")
    except Exception as e:
        log_message(f"[LOG TOOLS -> SEARCH REGEX] | [ERROR] Failed to search: {e}")
    
    return matches

def log_ping():
    """Issues a ping to the console.log file using RCON.\n
    Does not 'log your ping.'\n
    If the config files are missing, it will attempt to rebuild them first.
    """
    try:
        if not validate_configs():
            log_message("[LOG TOOLS -> LOG PING] | [WARNING] Missing or invalid config files. Rebuilding...")
            build_ping_config_files()

            if not validate_configs():
                log_message("[LOG TOOLS -> LOG PING] | [ERROR] Config files could not be created. Aborting.")
                return
            
        r_execute("exec powerplayping.cfg")
        log_message("[LOG TOOLS -> LOG PING] | [INFO] Attempted console ping. See rcon response for details.")

    except Exception as e:
        log_message(f"[LOG TOOLS -> LOG PING] | [ERROR] Failed to execute: {e}")
    
if __name__ == "__main__":
    search_string("PartyClientDbg")