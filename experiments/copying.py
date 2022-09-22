import time
import sys
from copy import copy

l1 = ["a"] * 1000

start_time = time.time()
l2 = l1[:]
end_time = time.time()

print("copy by list slicing: ", end_time - start_time)

start_time = time.time()
l3 = copy(l1)
end_time = time.time()

print("copy by module copy: ", end_time - start_time)
