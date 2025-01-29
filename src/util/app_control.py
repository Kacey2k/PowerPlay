from pathlib import Path
import sys
import psutil
import threading
import time

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from src.modules.debug import log_message
from src.util.rcon_handler import r_execute

TF2_OPENED = False
RCON_CONFIGURED = False
SESSION_ACTIVE = False
_STATUS_ = -1

TF2_BINARIES = {
    'alt': 'hl2.exe',
    'win64': 'tf_win64.exe',
    'win32': 'tf.exe',
}

def check_tf2():
    """Check if TF2 is open"""
    global TF2_OPENED
    for proc in psutil.process_iter():
        try:
            if proc.name() in TF2_BINARIES.values():
                TF2_OPENED = True
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    TF2_OPENED = False

def check_rcon():
    """Check if RCON is configured"""
    global RCON_CONFIGURED
    if r_execute('tf_party_chat "[PowerPlay] Successfully initialized!"') is not None:
        RCON_CONFIGURED = True
    else:
        RCON_CONFIGURED = False

def update_status():
    global _STATUS_
    if not TF2_OPENED:
        _STATUS_ = -1 # [HALT] Tf2 not opened
    elif TF2_OPENED and not RCON_CONFIGURED:
        _STATUS_ = 0 # [HALT] Tf2 opened but rcon not configured
    elif TF2_OPENED and RCON_CONFIGURED and not SESSION_ACTIVE:
        _STATUS_ = 1 # IDLE
    elif TF2_OPENED and RCON_CONFIGURED and SESSION_ACTIVE:
        _STATUS_ = 2 # ACTIVE

def app_controller():
    global RCON_CONFIGURED
    check_tf2()
    if TF2_OPENED:
        if not RCON_CONFIGURED:
            check_rcon()
            if RCON_CONFIGURED:
                log_message("[App Controller] | [Info] RCON configured successfully.")

        if RCON_CONFIGURED:
            threading.Event().wait(5)
        else:
            threading.Event().wait(1)
    else:
        RCON_CONFIGURED = False

    update_status()

    if _STATUS_ == -1:
        log_message("[App Controller] | [Warning] TF2 is not running and RCON is not configured.")
    elif _STATUS_ == 0:
        log_message("[App Controller] | [Warning] TF2 is running but RCON is not configured.")
    elif _STATUS_ == 1:
        log_message("[App Controller] | [Info] TF2 is running and RCON is configured but no session is active.")
    elif _STATUS_ == 2:
        log_message("[App Controller] | [Info] TF2 is running, RCON is configured, and a session is active.")

def status_checker():
    while True:
        app_controller()
        if _STATUS_ > 0:
            threading.Event().wait(10)
        else:
            threading.Event().wait(5)

def start_status_checker():
    check_thread = threading.Thread(target=status_checker)
    check_thread.daemon = True
    check_thread.start()

def super_ultra_mega_thread(): # TODO
    start_status_checker()
    # datastream startup

#if __name__ == "__main__":
#    start_status_checker()
#    while True:
#        time.sleep(1)