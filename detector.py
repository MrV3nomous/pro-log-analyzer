FAILED_LOGIN_KEYWORDS = [
    "failed password",
    "authentication failure",
    "login failed"
]

def detect_bruteforce(line):

    line = line.lower()

    for keyword in FAILED_LOGIN_KEYWORDS:
        if keyword in line:
            return True

    return False
