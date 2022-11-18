"""
Conclusion:
list(map(f, l)) is always slightly faster than list comprehension
Also, map() itself has little overhead.
So, in most cases, using built-in map() is better
unless there is an readability issue or something.
"""
from random import choice
from time import time, sleep
from string import digits

sum_dt1, sum_dt2, sum_dt3 = 0, 0, 0
worst_dt1, worst_dt2, worst_dt3 = 0, 0, 0


def experiment():
    global sum_dt1, sum_dt2, sum_dt3, worst_dt1, worst_dt2, worst_dt3
    arr = [choice(digits) for _ in range(3000)]

    # just create map object
    st1 = time()
    arr1 = map(int, arr)
    et1 = time()

    # list(map~)
    st2 = time()
    arr2 = list(map(int, arr))
    et2 = time()

    # list comprehension
    st3 = time()
    arr3 = [int(x) for x in arr]
    et3 = time()

    dt1 = (et1 - st1)
    dt2 = (et2 - st2)
    dt3 = (et3 - st3)

    sum_dt1 += dt1
    sum_dt2 += dt2
    sum_dt3 += dt3
    worst_dt1 = max(worst_dt1, dt1)
    worst_dt2 = max(worst_dt2, dt2)
    worst_dt3 = max(worst_dt3, dt3)

if __name__ == "__main__":
    for _ in range(100):
        for _ in range(50):
            experiment()
        sleep(0.2)
    
    print("< sum >")
    print(f"map:       {sum_dt1} seconds")
    print(f"list(map): {sum_dt2} seconds")
    print(f"comp:      {sum_dt3} seconds")
    
    print("\n< worst >")
    print(f"map:       {worst_dt1} seconds")
    print(f"list(map): {worst_dt2} seconds")
    print(f"comp:      {worst_dt3} seconds")
