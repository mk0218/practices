"""
list copying by copy.copy vs. list slicing
conclusion: little difference
(copy.deepcopy vs. list slicing은 언젠가..)
"""
import time
import sys
from copy import copy
from random import choice
from string import digits


def experiment():
    l1 = [choice(digits) for _ in range(3000)]

    start_time = time.time()
    l2 = l1[:]
    end_time = time.time()

    dt1 = end_time - start_time
    
    start_time = time.time()
    l3 = copy(l1)
    end_time = time.time()

    dt2 = end_time - start_time

    return dt1, dt2


if __name__ == "__main__":
    sum1, sum2 = 0, 0
    worst1, worst2 = 0, 0
    for _ in range(300):
        dt1, dt2 = experiment()
        sum1, sum2 = sum1 + dt1, sum2 + dt2
        worst1, worst2 = max(dt1, worst1), max(dt2, worst2)

    print("< sum >")
    print(f"list slicing: {sum1} seconds")
    print(f"copy.copy:    {sum2} seconds")
    print("\n< worst >")
    print(f"list slicing: {worst1} seconds")
    print(f"copy.copy:    {worst2} seconds")
