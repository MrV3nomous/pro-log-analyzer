from multiprocessing import Pool, cpu_count
from collections import Counter
import os

from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

from parallel_parser import process_chunk
from dashboard import generate_table
from utils import read_in_chunks
from exporter import export_json, export_csv


def analyze(path):
    """
    Analyze the log file using multiprocessing and streaming chunks.
    """

    level_total = Counter()
    ip_total = Counter()
    attack_total = Counter()

    with open(path, "r", errors="ignore") as f:

        pool = Pool(cpu_count())

        chunks = read_in_chunks(f)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
        ) as progress:

            task = progress.add_task("Processing logs...", total=None)

            with Live(
                generate_table(level_total, ip_total, attack_total),
                refresh_per_second=2,
            ) as live:

                for level, ip, attack in pool.imap(process_chunk, chunks):

                    level_total.update(level)
                    ip_total.update(ip)
                    attack_total.update(attack)

                    progress.update(task, advance=1)

                    live.update(
                        generate_table(level_total, ip_total, attack_total)
                    )

        pool.close()
        pool.join()

    return level_total, ip_total, attack_total


def get_valid_file():
    """
    Ask user for a log file path until a valid file is provided.
    """

    while True:

        path = input("Enter log file path: ").strip()

        if not path:
            print("Please enter a valid file path.\n")
            continue

        if not os.path.exists(path):
            print("Error: File not found. Please try again.\n")
            continue

        if not os.path.isfile(path):
            print("Error: Path is not a file.\n")
            continue

        return path


def main():

    print("\nPro Log Analyzer\n")

    try:

        path = get_valid_file()

        levels, ips, attacks = analyze(path)

    except PermissionError:

        print("\nError: Permission denied when accessing the file.\n")
        return

    except KeyboardInterrupt:

        print("\nProgram interrupted by user.\n")
        return

    data = {
        "levels": dict(levels),
        "ips": dict(ips),
        "attacks": dict(attacks),
    }

    print("\nAnalysis complete.\n")

    choice = input("Export report? (y/n): ").strip().lower()

    if choice == "y":

        export_json(data)
        export_csv(ips)

        print("Reports exported successfully.\n")

    print("Done.")


if __name__ == "__main__":
    main()
