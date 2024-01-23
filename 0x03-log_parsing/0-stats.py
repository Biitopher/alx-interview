#!/usr/bin/python3
"""Compute metrics to parse HTTP request logs"""
import sys
import re


def extract_input(input_line):
    """Regular expression to extract relevant information from input line"""
    log_pattern = (r'\s*(?P<ip>\S+)\s*',
                   r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
                   r'\s*"(?P<request>[^"]*)"\s*',
                   r'\s*(?P<status_code>\S+)',
                   r'\s*(?P<file_size>\d+)'
                   )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(log_pattern[0],
                                            log_pattern[1],
                                            log_pattern[2],
                                            log_pattern[3],
                                            log_pattern[4])
    match = re.fullmatch(log_format, input_line)
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_size, status_code_counts):
    """Print accumulated statistics"""
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_code_counts.keys()):
        num = status_code_counts.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_size, status_code_counts):
    """Update given HTTP request log"""
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_code_counts.keys():
        status_code_counts[status_code] += 1
    return total_size + line_info['file_size']


def run():
    """Start log parsering"""
    line_num = 0
    total_size = 0
    status_code_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_size = update_metrics(
                line,
                total_size,
                status_code_counts,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_code_counts)


if __name__ == '__main__':
    run()
