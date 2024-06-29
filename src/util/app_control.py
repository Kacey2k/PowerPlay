# This script initializes Rcon connection & Session controller

# There are 3 app states: ACTIVE, IDLE, WAITINGONTF

# ACTIVE: when a session is occuring, meaning status is returning data
# IDLE: when no session is occuring, meaning status is not returning data
# WAITINGONTF: means Team Fortress 2 is not running, thus other states are not possible

import configparser
import os
import sys
import rcon
import threading
from rcon.source import Client
from threading import Timer

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.modules.debug import log_message
from rcon_handler import r_execute

settings_file_path = os.path.join(os.path.dirname(__file__), '../../settings.ini')
config = configparser.ConfigParser()
config.read(settings_file_path)