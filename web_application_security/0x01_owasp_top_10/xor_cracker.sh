#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <base64_encoded_string>"
    exit 1
fi

encoded_str="$1"

python3 - <<EOF
import base64
import string

encoded_str = "$encoded_str"
decoded_bytes = base64.b64decode(encoded_str)

# Function to check if all characters are printable
def is_printable(s):
    return all(c in string.printable for c in s)

# Iterate through all possible single-byte XOR keys
for key in range(256):
    xored = bytes([b ^ key for b in decoded_bytes])
    try:
        xored_str = xored.decode('utf-8')
        if is_printable(xored_str):
            print(f"Key: {key} (0x{key:02x}) -> Password: {xored_str}")
    except UnicodeDecodeError:
        continue
EOF

