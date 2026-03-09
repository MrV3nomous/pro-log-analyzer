import random
import time

LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]
ENDPOINTS = ["/login", "/dashboard", "/api/data", "/logout", "/admin"]
MESSAGES = [
    "User login successful",
    "Disk usage high",
    "Database connection established",
    "Cache refreshed",
    "Service started"
]

FAILED_LOGIN = "Failed password for invalid user"

def random_ip():
    return ".".join(str(random.randint(1,255)) for _ in range(4))


def random_timestamp():

    return time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(random.randint(1600000000,1700000000))
    )


def generate_line():

    level = random.choice(LOG_LEVELS)
    ip = random_ip()
    endpoint = random.choice(ENDPOINTS)

    # 10% chance of failed login
    if random.random() < 0.1:
        message = FAILED_LOGIN
    else:
        message = random.choice(MESSAGES)

    return f"{random_timestamp()} [{level}] {ip} {endpoint} {message}\n"


def generate_file(filename, lines):

    with open(filename, "w") as f:

        for _ in range(lines):
            f.write(generate_line())


if __name__ == "__main__":

    print("Generating demo log file...")

    generate_file("demo_server.log", 5000000)

    print("Log file generated: demo_server.log")
