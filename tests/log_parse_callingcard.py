# Identifying "Session Calling Card" from sample data.

# This is likely not going to be used in the final product due to nuances in the way theses appear.

# TO USE:
# Place this file in the same directory as your log file
# Run the script, and it will output the number of unique "sessions" detected in the log file

import re
import os

def detect_session_calling_card():
    cardCount = 0

    dir = os.path.dirname(os.path.abspath(__file__))
    log = os.path.join(dir, 'log_parse_sample.log')

    pattern = re.compile(
        r"Team Fortress\s+"
        r"Map: .+\s+"
        r"Players: \d+ / \d+\s+"
        r"Build: \d+\s+"
        r"Server Number: \d+"
    )

    with open(log, 'r') as file:
        content = file.read()

    callingCards = pattern.findall(content)

    for callingCard in callingCards:
        cardCount += 1

    print(f"Unique Sessions Detected: {cardCount}")

detect_session_calling_card()
