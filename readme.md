# File Integrity Monitoring Tool

A Python-based desktop application that detects unauthorized modifications to files using the **SHA-256 hashing algorithm**. The application allows users to store the original hash values of selected files, verify their integrity at any time, and generate forensic reports indicating whether files have been altered.

---

## Features

- 🔒 SHA-256 based file integrity verification
- 📁 Monitor multiple files
- 💾 Automatically creates and stores file hashes in `hashes.json`
- 🔍 Verify file integrity anytime
- ⚠️ Detect modified or missing files
- 📄 Generate forensic verification reports
- 🖥️ User-friendly Tkinter GUI

---

## Technologies Used

- Python 3.x
- Tkinter
- hashlib
- JSON
- os
- datetime

---

## Project Structure

```
File-Integrity-Monitor/
│
├── main.py
├── FILEIN.ipynb
├── README.md
└── requirements.txt
```

> **Note:** The `hashes.json` file is **not included** in this repository. It is automatically created the first time you store file hashes.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-integrity-monitor.git
```

### 2. Navigate to the project directory

```bash
cd file-integrity-monitor
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## How It Works

### Step 1: Select Files

Choose one or more files that you want to monitor.

### Step 2: Store File Hashes

The application computes the SHA-256 hash of each selected file and automatically creates a `hashes.json` file (if it does not already exist) to store the hashes.

### Step 3: Verify Integrity

During verification, the application recalculates the SHA-256 hash of each monitored file and compares it with the previously stored hash.

Possible outcomes:

- ✅ **SAFE** – File has not been modified.
- ⚠️ **MODIFIED** – File contents have changed.
- ❌ **FILE NOT FOUND** – The monitored file is missing.

### Step 4: Generate Report

A timestamped forensic report is automatically generated after each verification.

Example:

```
sample.pdf   -> SAFE
notes.txt    -> MODIFIED
image.png    -> FILE NOT FOUND
```

---

## Applications

- Digital Forensics
- Cybersecurity Projects
- File Tamper Detection
- Evidence Integrity Verification
- Secure Document Monitoring
- System Administration

---

## Future Enhancements

- Real-time background monitoring
- Folder monitoring support
- Email notifications
- SQLite/MySQL database integration
- User authentication
- Digital signature verification
- Detailed verification history and analytics

---

## Author

**Vedant Bhor**

Computer Engineering Student

---

## License

This project is developed for educational and learning purposes. You are free to use, modify, and extend it for academic, research, and personal projects.