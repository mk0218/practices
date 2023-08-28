""" My own priority queue implementation using heapq. """
# both min and max priority queue available (Determine when creating a new instance.)
# a variety of data types available
# push(x), pop(), in, remove(x), and anythine else....
# support function as a parameter to compare values.
# 1. Implement min heap. (integer)
# 2. Implement max heap. (integer) Integrate with min heap.
# 3. Make those to accept any data type (and to compare values, too.)
# 4. Do some refactoring.
import heapq


class PriorityQueue:
    def __init__(self, descending=False):
        self._heap = []
        self._c = -1 if descending else 1  # coefficient

    def push(self, n):
        heapq.heappush(self._heap, (self._c * n))
    
    def pop(self):
        """ Raises IndexError when empty. """
        return (self._c * heapq.heappop(self._heap))


class MaxPriorityQueue:
    def __init__(self):
        self._heap = []
    
    def push(self, n):
        heapq.heappush(self._heap, (-1 * n))

    def pop(self):
        return (-1 * heapq.heappop(self._heap))