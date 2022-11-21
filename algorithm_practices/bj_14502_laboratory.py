'''
BAEKJOON 14502번 문제
https://www.acmicpc.net/problem/14502
[ 입력 ]
연구소의 크기 N(height), M(width) 3이상 8이하
N개의 줄에 지도의 모양 (0: 빈 칸, 1: 벽, 2: 바이러스)
[ 출력 ]
안전 영역의 최대 크기
'''
import sys
from copy import copy
from enum import IntEnum
from itertools import combinations, product


class Directions:
    eight = tuple(filter(lambda p: p != (0, 0), product((-1, 0, 1), repeat=2)))
    four = tuple(filter(lambda p: abs(p[0]*p[1]) != 1, eight))


class Matrix:

    def __init__(self, m):
        self._m = m
        self.width = len(m[0])
        self.height = len(m)

    def get(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        return self._m[y][x]

    def set(self, x, y, v):
        if x < 0 or y < 0:
            raise IndexError
        self._m[y][x] = v

    def setall(self, seq, v):
        for p in seq:
            self.set(*p, v)
    
    def valid(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def gen_indices(self):
        """ An indices generator (in order) """
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self._m)


class BS(IntEnum):
    EMPTY = 0
    WALL = 1
    VIRUS = 2

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.value)


class LabSimulator(Matrix):
    count = 0
    def __init__(self, m):
        super().__init__(m)
        self.initial_state = {state: set() for state in BS}
        for p in self.gen_indices():
            self.initial_state[self.get(*p)].add(p)
        self.empty = len(self.initial_state[BS.EMPTY])
    
    def _reset(self):
        self.setall(self.initial_state[BS.EMPTY], BS.EMPTY)
        self.empty = len(self.initial_state[BS.EMPTY])

    def _spread(self):
        visited = set()
    
        def condition(p):
            return p not in visited and self.get(*p) == BS.EMPTY

        def next_blocks(x, y):
            indices = ((x+dx, y+dy) for dx, dy in Directions.four)
            return filter(condition, indices)
            
        for x, y in self.initial_state[BS.VIRUS]:
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                try:
                    state = self.get(x, y)
                except IndexError:
                    continue
                if state == BS.WALL:
                    continue
                visited.add((x, y))
                stack += ((x+dx, y+dy) for dx, dy in Directions.four)
                if state == BS.EMPTY:
                    self.set(x, y, BS.VIRUS)
                    self.empty -= 1



    def _simulate(self, blocks):
        self.setall(blocks, BS.WALL)
        self.empty -= 3
        self._spread()
        count_empty = self.empty
        self._reset()
        return count_empty
            
    def run(self):

        def alone(blocks):
            for (x, y), (dx, dy) in product(blocks, Directions.eight):
                try:
                    value = self.get(x+dx, y+dy)
                except:
                    continue
                if value != BS.EMPTY:
                    return False
            return True

        max_safezone = 0
        for blocks in combinations(self.initial_state[BS.EMPTY], 3):
            if not alone(blocks):
                max_safezone = max(max_safezone, self._simulate(blocks))

        return max_safezone


if __name__ == "__main__":
    readl = sys.stdin.readline
    h, w = map(int, readl().split())
    sim = LabSimulator([[int(c) for c in readl().split()] for _ in range(h)])

    print(sim.run())

                                          