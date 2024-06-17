# app states: active, idle, waitingonTF
# session states: active, waiting
# this script will piggie-back off of a session controller
import os

# from src.util.session_controller import SessionController

# Mockup of how session state may be implemented
current_host_header = "123.123.123.123, ctf_2fort"
previous_host_header = "100.777.888.999, pl_badwater"

def terminate_session():
    print("[session_state.py] Terminating session...")
    # terminate session

if current_host_header != previous_host_header:
    terminate_session() # generates a new session if we are not waiting
else:
    print("[session_state.py] Session is active...")