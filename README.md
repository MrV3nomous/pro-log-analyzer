## 🚀 Pro Log Analyzer

Real-time log analysis tool built in Python with multiprocessing and a live terminal dashboard.

Pro Log Analyzer is a high-performance command-line application designed to process very large server log files efficiently.
It uses stream processing and multiprocessing to analyze logs without loading the entire file into memory.

---

## ✨ Features


✔ High-performance parsing using multiprocessing

✔ Handles huge log files (10GB+ supported)

✔ Live terminal dashboard for real-time metrics

✔ Progress bar during analysis

✔ Detects suspicious activity like repeated failed logins

✔ Extracts and counts IP addresses

✔ Exports reports to JSON and CSV

✔ Graceful error handling

---

## 🖥️ Example Dashboard

While analyzing a log file, the program displays a live dashboard showing:

- Log level statistics
- Most active IP addresses
- Suspicious login activity

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MrV3nomous/pro-log-analyzer.git

cd pro-log-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```


---


## ▶️ Usage

Run the analyzer:

```bash
python analyzer.py
```

Then enter the path to the log file:

Enter log file path: server.log

The program will analyze the file and display the live monitoring dashboard.


---


## 🧪 Generating Demo Logs

A log generator is included for testing.

Run:

```bash
python generate_demo_logs.py
```

This will generate a file called:

demo_server.log

You can increase the number of lines in the script to simulate very large log files.


---


## 📊 Exported Reports

After analysis, the tool can export reports:

JSON Report

- Summary of log statistics
- Suspicious activity data

CSV Report

- IP activity counts

These files will be saved in the project directory.


---


## 📝 Example Log Format

The analyzer expects logs similar to:


2023-11-15 10:23:11 [INFO] 192.168.1.12 /login User login successful

2023-11-15 10:23:12 [ERROR] 45.33.21.9 /login Failed password for invalid user

2023-11-15 10:23:14 [WARNING] 10.0.0.5 /dashboard Disk usage high


---


## 📦 Requirements

- Python 3.8+
- Rich library for terminal UI

Install dependencies with:

```bash
pip install -r requirements.txt
```

---


## 📜 License

This project is provided for educational and demonstration purposes.


---


## 👨‍💻 Author

Raj

---

⭐ If you found this project useful, consider giving the repository a star!
