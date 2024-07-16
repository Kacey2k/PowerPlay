import os
import sys
import rcon
import threading
from rcon.source import Client
from threading import Timer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.modules.debug import log_message
from config import check_config, cfg_rcon_ip, cfg_rcon_port, cfg_rcon_password

def r_execute(rcon_command):
    """Accepts input as RCON Commands\n
    Requires RCON settings to be properly configured in settings.ini"""
    check_config()

    try:
        rcon_ip = cfg_rcon_ip
        rcon_port = cfg_rcon_port
        rcon_password = cfg_rcon_password
    except Exception as e:
        log_message(f"[Rcon] | [Error] Missing RCON settings in settings.ini: {e}")
        return

    try:
        with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
            response = client.run(rcon_command)
            log_message(f"[Rcon] | [Info] Command sent: {rcon_command}")
            return response
    except Exception as e:
        log_message(f"[Rcon] | [Error] Failed to execute command '{rcon_command}': {e}")