#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    count_keys = [0]
    boxes_numbers = len(boxes)

    for keys in count_keys:
        for box in boxes[keys]:
            if box < boxes_numbers and box not in count_keys:
                count_keys.append(box)
    if len(count_keys) == boxes_numbers:
        return True
    return False
