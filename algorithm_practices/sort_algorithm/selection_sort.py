import sys
from typing import List

nums = list(map(int, sys.stdin.readline().split()))


def selection_sort(src: List[int]):
    cursor = 0
    while cursor < len(nums):
        minidx = cursor
        for i in range(cursor, len(src)):
            if src[i] < src[minidx]:
                minidx = i
        src[cursor], src[minidx] = src[minidx], src[cursor]
        cursor += 1
    return src
