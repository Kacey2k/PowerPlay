import subprocess

# STEAM = r"C:\Program Files (x86)\Steam\steam.exe"
STEAM = r"Steam DIR HERE"

subprocess.Popen([STEAM, "-applaunch", "440", "-rpt", "-usercon", "-windowed", "-novid", "-w", "1280", "-h", "720"])

# ok so this works, nice.