import json
import csv


def export_json(data, filename="report.json"):

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def export_csv(counter, filename="ips.csv"):

    with open(filename, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["IP", "Requests"])

        for ip, count in counter.items():
            writer.writerow([ip, count])
