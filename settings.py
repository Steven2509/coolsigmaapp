# settings.py
import os

SETTINGS_FILE = "data.txt"

def get_setting(key, default=""):
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(f"{key}="):
                    return line.strip().split("=", 1)[1]
    except FileNotFoundError:
        return default
    return default

def set_setting(key, value):
    lines = []
    found = False
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(f"{key}="):
                    lines.append(f"{key}={value}\n")
                    found = True
                else:
                    lines.append(line)
    except FileNotFoundError:
        pass

    if not found:
        lines.append(f"{key}={value}\n")

    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

