from pathlib import Path
import sys

root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root))

from src.util.app_control import SESSION_ACTIVE

# TODO

# scan our current runtime datastream for lobby configuration changes (new lobby, new map, etc)
# upon detection, terminate previous session, generate new session, and update SESSION_ACTIVE
