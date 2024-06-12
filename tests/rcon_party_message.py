import rcon
import threading
from rcon.source import Client

# Using generic client parameters
rcon_ip = "127.0.0.1"
rcon_port = 27015
rcon_password = "your_rcon_password"

def party_message():
    """Command to be sent to TeamFortress 2"""
    with Client(rcon_ip, rcon_port, passwd=rcon_password) as client:
        message = "Hello, world!"
        response = client.run(f'tf_party_chat "{message}"')
    print(response)

party_message()