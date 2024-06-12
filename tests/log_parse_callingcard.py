# Identifying "Session Calling Card" from sample data

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