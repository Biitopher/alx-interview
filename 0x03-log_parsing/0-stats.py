#!/usr/bin/python3
"""Compute metrics"""
import sys
import re


def parse_line(line):
    """Regular expression to extract relevant information from input line"""
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\]
            "GET /projects/260 HTTP/1.1" (\d+) (\d+)')
    match = pattern.match(line)

    if match:
        ip_address, status_code, file_size = match.groups()
        return ip_address, int(status_code), int(file_size)
    else:
        return None

def print_statistics(total_size, status_code_counts):
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

def main():
    total_size = 0
    status_code_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            data = parse_line(line)

            if data:
                ip_address, status_code, file_size = data
                total_size += file_size

                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code_counts)

if __name__ == "__main__":
    main()
