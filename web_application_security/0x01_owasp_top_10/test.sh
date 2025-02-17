#!/bin/bash
# Check if input starts with {xor}
if [[ "$1" != {xor}* ]]; then
    echo "Usage: $0 {xor}<base64_encoded_string>"
    exit 1
fi

# Remove the {xor} prefix
encoded_str="${1#\{xor\}}"

# Define the multi-byte XOR key as a hex string
# Update this key based on Task 1's script or repository clues
xor_key_hex="5eab5f5f"

# Convert the hex key to raw bytes
xor_key=$(echo "$xor_key_hex" | xxd -r -p)

# Decode and apply multi-byte XOR using Python
python3 - <<EOF
import base64
import binascii

encoded_str = "$encoded_str"
xor_key = b"$xor_key"

# Decode from Base64
decoded_bytes = base64.b64decode(encoded_str)

# Repeat the key to match the length of decoded_bytes
repeated_key = (xor_key * (len(decoded_bytes) // len(xor_key) + 1))[:len(decoded_bytes)]

# Apply XOR
xored_bytes = bytes([b ^ k for b, k in zip(decoded_bytes, repeated_key)])

# Output the result in hexadecimal
print(binascii.hexlify(xored_bytes).decode('utf-8'))
EOF

