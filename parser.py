import re

LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

def extract_ips(line):
    return re.findall(ip_pattern, line)

def detect_log_level(line):

    for level in LOG_LEVELS:
        if level in line:
            return level

    return "UNKNOWN"
