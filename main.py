import hashlib
import json
import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


# ------------------------------
# 1. Calculate SHA-256 hash
# ------------------------------
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None


# ------------------------------
# 2. Store initial hashes
# ------------------------------
def store_hashes(file_paths, db_file="hashes.json"):
    hashes = {}
    for file_path in file_paths:
        file_hash = calculate_hash(file_path)
        if file_hash:
            hashes[file_path] = file_hash
    with open(db_file, "w") as f:
        json.dump(hashes, f)
    messagebox.showinfo("✅ Success", f"Hashes stored in {db_file}")


# ------------------------------
# 3. Verify all files
# ------------------------------
def verify_all(db_file="hashes.json"):
    if not os.path.exists(db_file):
        messagebox.showerror("⚠️ Error", "No stored hashes found. Run 'Store Hashes' first.")
        return None

    with open(db_file, "r") as f:
        stored_hashes = json.load(f)

    results = {}
    for file_path, old_hash in stored_hashes.items():
        new_hash = calculate_hash(file_path)
        if not new_hash:
            status = "❌ File not found"
        elif old_hash == new_hash:
            status = "✅ SAFE"
        else:
            status = "⚠️ MODIFIED"
        results[file_path] = status
    return results


# ------------------------------
# 4. Generate forensic report
# ------------------------------
def generate_report(results, report_dir="."):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"Forensic_Report_{timestamp}.txt"
    report_path = os.path.join(report_dir, report_name)

    with open(report_path, "w", encoding="utf-8") as report:
        for file_path, status in results.items():
            line = f"{file_path} → {status}\n"
            report.write(line)

    messagebox.showinfo("📄 Report Generated", f"Forensic report saved at:\n{report_path}")


