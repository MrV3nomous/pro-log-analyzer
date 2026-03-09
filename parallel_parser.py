from collections import Counter
from parser import extract_ips, detect_log_level
from detector import detect_bruteforce


def process_chunk(lines):

    level_counter = Counter()
    ip_counter = Counter()
    attack_counter = Counter()

    for line in lines:

        level = detect_log_level(line)
        level_counter[level] += 1

        ips = extract_ips(line)

        for ip in ips:

            ip_counter[ip] += 1

            if detect_bruteforce(line):
                attack_counter[ip] += 1

    return level_counter, ip_counter, attack_counter
