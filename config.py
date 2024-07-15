import configparser
import os

from src.modules.debug import log_message

cfg_app_state = 0
cfg_app_debug = 1
cfg_app_notification = 1
cfg_rcon_ip = "127.0.0.1"
cfg_rcon_password = "your_rcon_password"
cfg_rcon_port = 27015
cfg_user_api_key = ""
cfg_user_directory = ""
cfg_user_language = ""
cfg_user_steamid = ""

def check_config():
    """Reads settings.ini and sets global variables for each setting.\n
    Run this function before importing a variable to ensure the most up-to-date value.\n
    Variables:\n
    cfg_app_state (0 = Not configured, 1 = Configured)\n
    cfg_app_debug (0 = No debug, 1 = Debug enabled)\n
    cfg_app_notification (0 = No notifications, 1 = Debug notifications)\n
    cfg_rcon_ip (127.0.0.1 required)\n
    cfg_rcon_password (String for rcon authentication set by user)\n
    cfg_rcon_port (Int for rcon communication controlled by user)\n
    cfg_user_api_key (String for steam API access)\n
    cfg_user_directory (TeamFortress 2 local directory location as string)\n
    cfg_user_language (User's localization setting)\n
    cfg_user_steamid (SteamID for current user)"""
    global cfg_app_state
    global cfg_app_debug
    global cfg_app_notification
    global cfg_rcon_ip
    global cfg_rcon_password
    global cfg_rcon_port
    global cfg_user_api_key
    global cfg_user_directory
    global cfg_user_language
    global cfg_user_steamid

    # check for whether the settings.ini file exists
    if not os.path.exists('settings.ini'):
        log_message("[CONFIG] | [Warning] settings.ini not found, creating a new one. Recommend restarting.")
        config = configparser.ConfigParser()
        config['app'] = {
            'state': 0,
            'debug': 0,
            'notification': 1
        }
        config['rcon'] = {
            'rcon_ip': '',
            'rcon_password': '',
            'rcon_port': 27015
        }
        config['user'] = {
            'api_key': '',
            'directory': '',
            'language': '',
            'steamid': ''
        }
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
    else:
        config = configparser.ConfigParser()
        config.read('settings.ini')
        cfg_app_state = config.getint('app', 'state')
        cfg_app_debug = config.getint('app', 'debug')
        cfg_app_notification = config.getint('app', 'notification')
        cfg_rcon_ip = config.get('rcon', 'rcon_ip')
        cfg_rcon_password = config.get('rcon', 'rcon_password')
        cfg_rcon_port = config.getint('rcon', 'rcon_port')
        cfg_user_api_key = config.get('user', 'api_key')
        cfg_user_directory = config.get('user', 'directory')
        cfg_user_language = config.get('user', 'language')
        cfg_user_steamid = config.get('user', 'steamid')
        log_message("[CONFIG] | [Info] Global configuration variables refreshed.")