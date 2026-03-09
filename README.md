##Pro Log Analyzer

A high-performance command-line tool for analyzing large server log files in real time.

Pro Log Analyzer processes log files efficiently using multiprocessing and stream processing, allowing it to handle logs that are several gigabytes in size without loading the entire file into memory.

---

Features

- Fast log parsing using multiprocessing
- Stream processing for handling very large files (10GB+)
- Real-time terminal dashboard
- Live progress bar during analysis
- Detection of suspicious activity such as repeated failed logins
- Extraction and counting of IP addresses
- Export results to JSON and CSV
- Graceful error handling for invalid file paths and permissions

---

Project Structure

pro-log-analyzer
│
├── analyzer.py
├── parser.py
├── detector.py
├── parallel_parser.py
├── dashboard.py
├── utils.py
├── exporter.py
├── generate_demo_logs.py
├── requirements.txt
└── README.md

---

Installation

Clone the repository:

git clone https://github.com/MrV3nomous/pro-log-analyzer.git
cd pro-log-analyzer

Install dependencies:

pip install -r requirements.txt

---

Usage

Run the analyzer:

python analyzer.py

Then enter the path to the log file when prompted.

Example:

Enter log file path: server.log

The program will analyze the log file and display a live dashboard showing log levels, most active IPs, and suspicious activity.

---

Example Log Format

The analyzer expects logs that contain timestamps, log levels, and IP addresses. For example:

2023-11-15 10:23:11 [INFO] 192.168.1.12 /login User login successful
2023-11-15 10:23:12 [ERROR] 45.33.21.9 /login Failed password for invalid user
2023-11-15 10:23:14 [WARNING] 10.0.0.5 /dashboard Disk usage high

---

Generating Demo Logs

You can generate a large test log file using the included script:

python generate_demo_logs.py

This will create a file named:

demo_server.log

You can adjust the number of lines in the script to generate logs of different sizes for testing.

---

Exporting Reports

After analysis, the program can export reports:

- JSON report containing summarized statistics
- CSV report containing IP activity

These files will be saved in the project directory.

---

Example Output

The program displays a live terminal dashboard showing:

- Log level counts
- Most frequent IP addresses
- Suspicious IP activity

---

Requirements

- Python 3.8+
- Rich library for terminal UI

Install dependencies with:

pip install -r requirements.txt

---

License

This project is provided for educational and demonstration purposes.

---

Author

Raj
