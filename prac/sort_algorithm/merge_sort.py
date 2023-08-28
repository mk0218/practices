import sys
from typing import List

nums = list(map(int, sys.stdin.readline().split()))


def merge(a: List[int], b: List[int]) -> List[int]:
    i, j, c = 0, 0, []
    while (i < len(a) and j < len(b)):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def merge_sort_1(src: List[int]) -> List[int]:
    if len(src) < 2:
        return src
    chunk1 = merge_sort_1(src[:len(src) // 2])
    chunk2 = merge_sort_1(src[len(src) // 2:])
    return merge(chunk1, chunk2)
