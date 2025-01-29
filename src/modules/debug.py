from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
import logging
from pathlib import Path
from datetime import datetime

global_debug_log = None

log_dir = Path.cwd() / 'data' / 'logs'
log_dir.mkdir(parents=True, exist_ok=True)
log_filename = log_dir / f'PowerPlayLog_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

def debug_tab(notebook):
    global global_debug_log
    debug_tab = QWidget()
    layout = QVBoxLayout()
    debug_tab.setLayout(layout)
    notebook.addTab(debug_tab, "Debug")

    debug_label = QLabel("PowerPlay Debug Log")
    debug_label.setStyleSheet("color: white; font: 14pt Arial;")
    layout.addWidget(debug_label)

    debug_log = QTextEdit()
    debug_log.setReadOnly(True)
    debug_log.setStyleSheet("background-color: #333333; color: white; font: 12pt Consolas;")
    debug_log.append("[***PowerPlay Debug Log***]")
    layout.addWidget(debug_log)

    global_debug_log = debug_log

def log_message(message):
    """Logs a message to the current debug log and GUI console.\n
    Logs located in data/logs/PowerPlayLog_YYYYMMDD_HHMMSS.log\n
    Make sure to set debug mode to 1 in settings.ini to view logs."""
    if global_debug_log is not None:
        global_debug_log.append(message)
    logging.debug(message)
