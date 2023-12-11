#!/usr/bin/python3
"""This module is a script"""
import sys
import signal
from collections import defaultdict


def signal_handler(sig, frame):
    """Handles signal"""
    print_stats()
    sys.exit(0)


def print_stats():
    """Prints statistics"""
    print(f"File size: {total_file_size}")

    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


total_file_size = 0
status_codes = defaultdict(int)
line_count = 0

valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in valid_status_codes and file_size.isdigit():
                status_codes[status_code] += 1
            total_file_size += int(file_size)

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    pass

print_stats()
sys.exit(0)
