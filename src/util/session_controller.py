import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.util.app_control import SESSION_ACTIVE

# TODO

# scan our current runtime datastream for lobby configuration changes (new lobby, new map, etc)
# upon detection, terminate previous session, generate new session, and update SESSION_ACTIVE
