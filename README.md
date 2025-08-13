# Nmap Network Scanner

A Python script to perform Nmap scans on a target IP or hostname and save detailed results automatically. Ideal for learning and small-scale network scanning tasks.

---

## Features
- Runs a detailed Nmap scan using `-A -T4` options.
- Automatically saves scan results in a timestamped file.
- Easy command-line usage.
- Organized results folder for easy tracking.

---

## Requirements
- Python 3.x
- Nmap installed on your system
- Linux, macOS, or Windows with Python support

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Sai-teja-007/nmap-network-scanner.git
cd nmap-network-scanner


```



2. **Ensure Python 3 and Nmap are installed**

```bash
python3 --version
nmap --version
```

3. **Create a results folder**

```bash
mkdir results
```

---

## Usage

```bash
python3 network_scanner.py <target-IP-or-hostname>
```

**Example:**

```bash
python3 network_scanner.py scanme.nmap.org
```

The scan output will be printed to the terminal and saved in the `results/` folder with a timestamped filename, e.g., `nmap_scan_20250813_150245.txt`.

---

## Folder Structure

```
nmap-network-scanner/
│
├── network_scanner.py      # Main Python scan script
├── README.md              # This file
└── results/               # Folder to store scan results
```

---

## How It Works

* The script takes a single target IP or hostname as input.
* Runs an Nmap scan with `-A -T4` (aggressive scan, faster timing).
* Captures the output and saves it in a uniquely named file in the `results/` folder.
* Prints scan output to the terminal for immediate review.

---

## Notes & Improvements

* Make sure you have permission to scan the target network.
* You can modify Nmap options in the script for customized scanning.
* This is a basic scanner for learning purposes; do not use it for unauthorized scanning.

---

## Disclaimer

This tool is intended for educational purposes only. Scanning networks without permission is illegal and unethical. Use responsibly.


