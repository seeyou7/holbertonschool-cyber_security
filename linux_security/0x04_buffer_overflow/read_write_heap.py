#!/usr/bin/env python3
"""
Usage: read_write_heap.py pid search_string replace_string

Searches the heap of a running process for `search_string` and replaces
it with `replace_string`. Only the first occurrence is replaced, but
this can be adapted if needed.
"""
import sys
import os

def usage():
    print(f"Usage: {sys.argv[0]} pid search_string replace_string")
    sys.exit(1)

def main():
    # --- 1) Validate and parse arguments ---
    if len(sys.argv) != 4:
        usage()

    pid, search_string, replace_string = sys.argv[1], sys.argv[2], sys.argv[3]

    # --- 2) Find the [heap] region in /proc/<pid>/maps ---
    heap_start = None
    heap_end = None
    maps_path = f"/proc/{pid}/maps"

    if not os.path.exists(maps_path):
        print(f"Error: Process {pid} does not exist or /proc/{pid}/maps is missing.")
        sys.exit(1)

    with open(maps_path, "r") as maps_file:
        for line in maps_file:
            if "[heap]" in line:
                # Format:  addr_start-addr_end perms offset dev inode [pathname]
                addr_range = line.split()[0]
                perms = line.split()[1]
                if 'r' not in perms or 'w' not in perms:  # we need read+write
                    print("Error: Heap region not readable/writable.")
                    sys.exit(1)

                heap_start, heap_end = addr_range.split('-')
                heap_start = int(heap_start, 16)
                heap_end = int(heap_end, 16)
                break

    if heap_start is None or heap_end is None:
        print("Error: Could not find [heap] region in maps.")
        sys.exit(1)

    # --- 3) Read the heap from /proc/<pid>/mem ---
    mem_path = f"/proc/{pid}/mem"

    if not os.path.exists(mem_path):
        print(f"Error: /proc/{pid}/mem does not exist.")
        sys.exit(1)

    try:
        with open(mem_path, "rb+") as mem_file:
            # Seek to the start of the heap
            mem_file.seek(heap_start)
            
            # Read heap into 'heap_data'
            heap_size = heap_end - heap_start
            heap_data = mem_file.read(heap_size)

            # --- 4) Search and replace the string in the heap_data ---
            search_bytes = search_string.encode()
            replace_bytes = replace_string.encode()

            idx = heap_data.find(search_bytes)
            if idx == -1:
                print(f"'{search_string}' not found in heap.")
                sys.exit(0)

            # Build the replaced data
            replaced_data = (heap_data[:idx] 
                             + replace_bytes 
                             + heap_data[idx + len(search_bytes):])

            # Move file pointer back to the start of the heap
            mem_file.seek(heap_start)
            # Write our modified data
            mem_file.write(replaced_data)

            print(f"Replaced '{search_string}' with '{replace_string}' in process {pid}'s heap.")

    except PermissionError:
        print("Permission denied. Try running as root (sudo).")
        sys.exit(1)

if __name__ == "__main__":
    main()

