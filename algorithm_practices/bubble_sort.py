from typing import List
import sys
import time

nums = list(map(int, sys.stdin.readline().split()))


def bubble_sort(nums: List[int]):
    for cnt in range(len(nums) - 1):
        for i in range(len(nums) - 1 - cnt):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


start_time = time.time()
bubble_sort(nums)
end_time = time.time()
print("result: ", nums)
print("time: ", end_time - start_time)
