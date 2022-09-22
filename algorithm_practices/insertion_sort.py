import time
import sys
from typing import List

nums = list(map(int, sys.stdin.readline().split()))


def insertion_sort(src: List[int]):
    cursor = 1
    while cursor < len(nums):
        for i in range(cursor, 0, -1):
            if src[i] < src[i - 1]:
                src[i], src[i - 1] = src[i - 1], src[i]
            else:
                break
        cursor += 1


start_time = time.time()
insertion_sort(nums)
end_time = time.time()
print("result: ", nums)
print("time: ", end_time - start_time)
