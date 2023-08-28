from typing import List


def insertion_sort(src: List[int]):
    cursor = 1
    while cursor < len(src):
        for i in range(cursor, 0, -1):
            if src[i] < src[i - 1]:
                src[i], src[i - 1] = src[i - 1], src[i]
            else:
                break
        cursor += 1
