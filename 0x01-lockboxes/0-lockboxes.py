#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set()
    keys.add(0)
    opened = {0}

    while keys:
        key = keys.pop()
        box = boxes[key]
        for k in box:
            if k not in opened:
                keys.add(k)
                opened.add(k)

    return len(opened) == len(boxes)
