from rich.table import Table

def generate_table(level_counter, ip_counter, attack_counter):

    table = Table(title="Pro Log Analyzer Dashboard")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    for level, count in level_counter.items():
        table.add_row(f"{level} logs", str(count))

    for ip, count in ip_counter.most_common(5):
        table.add_row(f"Top IP {ip}", str(count))

    for ip, count in attack_counter.items():

        if count > 5:
            table.add_row("Suspicious IP", ip)

    return table
