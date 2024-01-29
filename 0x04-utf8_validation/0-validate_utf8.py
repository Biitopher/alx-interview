#!/usr/bin/python3
"""Validation"""


def validUTF8(data):
    """Helper function to check if a given byte is a valid UTF-8 start byte"""
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b0

    def is_following_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        num_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        if num_bytes == 0:
            num_bytes = 1
        elif num_bytes > 4 or num_bytes == 1:
            return False

        i += 1
        for _ in range(num_bytes - 1):
            if i >= len(data) or not is_following_byte(data[i]):
                return False
            i += 1

    return True
