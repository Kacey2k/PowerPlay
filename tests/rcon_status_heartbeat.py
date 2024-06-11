import configparser
import os
import rcon
import threading
from rcon.source import Client
from threading import Timer

settings_file_path = os.path.join(os.path.dirname(__file__), '../settings.ini')
config = configparser.ConfigParser()
config.read(settings_file_path)

try:
    rcon_ip = config['rcon']['rcon_ip']
    rcon_port = int(config['rcon']['rcon_port'])
    rcon_password = config['rcon']['rcon_password']
except KeyError as e:
    raise KeyError(f"Key {e} not found in the 'rcon' section of the settings file")

attempt = 0

def heartbeat():
    """Command to be sent to TeamFortress 2"""
    with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
        global attempt
        attempt += 1
        response = client.run('status')
        print(f"Trying Status Heartbeat. . . Attempt: {attempt}")

def timerLoop():
    heartbeat()
    t = Timer(5.0, timerLoop)
    t.start() 

timerLoop()