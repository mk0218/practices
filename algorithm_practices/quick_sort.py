import time
import sys
from typing import List

nums = list(map(int, sys.stdin.readline().split()))

func_called = 0


# Quicksort는 코드짜기가 Quick한게 특징이건만
def quick_sort(src: List[int]) -> List[int]:
    global func_called
    func_called += 1
    if (n := len(src)) <= 1:
        return src
    if n <= 3:
        pval = src[0]
    else:
        pval = quick_sort([src[0], src[n // 2], src[-1]])[1]
    left, center, right = [], [], []
    for i in range(n):
        if src[i] < pval:
            left.append(src[i])
        elif src[i] > pval:
            right.append(src[i])
        else:
            center.append(src[i])

    left = quick_sort(left)
    right = quick_sort(right)
    return left + center + right


start_time = time.time()
result = quick_sort(nums)
end_time = time.time()
print("result: ", result)
print("time: ", end_time - start_time)
print("called: ", func_called)
