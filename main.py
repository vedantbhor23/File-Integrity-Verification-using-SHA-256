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


