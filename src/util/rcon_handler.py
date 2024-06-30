import configparser
import os
import rcon
import threading
from rcon.source import Client
from threading import Timer
from src.modules.debug import log_message

def r_execute(rcon_command):
    """Accepts input as RCON Commands
    Requires RCON settings to be properly configured in settings.ini"""
    settings_file_path = os.path.join(os.path.dirname(__file__), '../../settings.ini')
    config = configparser.ConfigParser()
    config.read(settings_file_path)

    try:
        rcon_ip = config['rcon']['rcon_ip']
        rcon_port = int(config['rcon']['rcon_port'])
        rcon_password = config['rcon']['rcon_password']
    except KeyError as e:
        log_message(f"Key {e} not found in the 'rcon' section of the settings file")
        return

    try:
        with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
            response = client.run(rcon_command)
            log_message(f"[Rcon] Command sent: {rcon_command}")
            return response
    except Exception as e:
        log_message(f"[Rcon] Failed to execute command '{rcon_command}': {e}")
    
def r_debug_confirmation():
    r_execute('tf_party_chat "[PowerPlay] TF2 Connection Established!"')

def r_debug_s_nolobby():
    r_execute('tf_party_chat "[PowerPlay] No Active Session Detected."')

def r_debug_s_islobby():
    r_execute('tf_party_chat "[PowerPlay] Active Session Detected."')

def r_status():
    """Send status command to TF2"""
    r_execute('status')

def r_heartbeat_timerLoop():
    """5 second timer for status command"""
    r_status()
    t = Timer(5.0, r_heartbeat_timerLoop)
    t.start()