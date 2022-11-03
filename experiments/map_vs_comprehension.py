from random import choice
from time import time, sleep
from string import digits

sum_dt1, sum_dt2 = 0, 0
worst_dt1, worst_dt2 = 0, 0


def experiment():
    global sum_dt1, sum_dt2, worst_dt1, worst_dt2
    arr = [choice(digits) for _ in range(3000)]

    st1 = time()
    arr1 = list(map(int, arr))
    et1 = time()

    st2 = time()
    arr2 = [int(x) for x in arr]
    et2 = time()

    dt1 = (et1 - st1)
    dt2 = (et2 - st2)

    sum_dt1 += dt1
    sum_dt2 += dt2
    worst_dt1 = max(worst_dt1, dt1)
    worst_dt2 = max(worst_dt2, dt2)


for _ in range(100):
    for _ in range(400):
        experiment()
    sleep(0.5)

print("< sum >")
print("map:  ", sum_dt1)
print("comp: ", sum_dt2)

print("\n< worst >")
print("map:  ", worst_dt1)
print("comp: ", worst_dt2)
