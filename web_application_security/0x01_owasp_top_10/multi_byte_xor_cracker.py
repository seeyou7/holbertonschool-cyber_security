import base64
import string
from itertools import product

# Encoded password_hash
password_hash = "Dz58bBlrNiUzPiovODdmGy4xMCMVFjVuDg=="

# Decode from Base64
decoded_bytes = base64.b64decode(password_hash)

# Define possible key lengths (e.g., 2 to 4 bytes)
min_key_length = 2
max_key_length = 4

# Define the character set for keys (printable ASCII)
key_chars = string.ascii_letters + string.digits + string.punctuation

# Function to check if all characters in a string are printable
def is_printable(s):
    return all(c in string.printable for c in s)

# Iterate through key lengths
for key_length in range(min_key_length, max_key_length + 1):
    print(f"Trying key length: {key_length}")
    # Generate all possible key combinations for the given length
    for key_tuple in product(key_chars, repeat=key_length):
        key = ''.join(key_tuple)
        key_bytes = key.encode()
        # Repeat the key to match the length of decoded_bytes
        repeated_key = (key_bytes * (len(decoded_bytes) // key_length + 1))[:len(decoded_bytes)]
        # Apply XOR
        xored_bytes = bytes([b ^ k for b, k in zip(decoded_bytes, repeated_key)])
        try:
            xored_str = xored_bytes.decode('utf-8')
            if is_printable(xored_str):
                print(f"Key: {key} -> Password: {xored_str}")
        except UnicodeDecodeError:
            continue

