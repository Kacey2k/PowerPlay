# If status less than or equal to 0, halt logging.

# CONSOLE.LOG NOTES:
# - Encoded in ANSI
# - Could have timestamps
# - Some data uses multiple lines
# - Data that uses multiple lines sometimes is not presented chronologically, "status" is a repeat offender

import sys
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root)

from src.modules.debug import log_message
from src.util.log_tools import logging_ready, log_exists


CONSOLE_LOGGING_ACTIVE = False

def preliminary_checks():
    """Run each time Status updated"""
    if not log_exists():
        return False
    if not logging_ready():
        return False
    return True
    
def main():
    if not preliminary_checks():
        return log_message("[LOGGER] | [WARNING] Logging halted (Did not pass preliminary checks).")
        # Maybe add a timer to retry
    else:
        log_message("[LOGGER] | [INFO] Logging initialized.")
        global CONSOLE_LOGGING_ACTIVE
        CONSOLE_LOGGING_ACTIVE = True

if __name__ == "__main__":
    main()