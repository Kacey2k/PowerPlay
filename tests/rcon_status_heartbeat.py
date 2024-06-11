import rcon
import threading
from rcon.source import Client
from threading import Timer

# Using generic client parameters
rcon_ip = "127.0.0.1"
rcon_port = 27015
rcon_password = "your_rcon_password"
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