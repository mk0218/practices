'''
BAEKJOON 14502번 문제
https://www.acmicpc.net/problem/14502
이게 다 오늘 고른 문제가 생각보다 넘 쉬워서 그래
이제 이거 오늘안에 안풀린다
[ 입력 ]
연구소의 크기 N(height), M(width) 3이상 8이하
N개의 줄에 지도의 모양 (0: 빈 칸, 1: 벽, 2: 바이러스)
[ 출력 ]
안전 영역의 최대 크기
'''
import sys
from copy import deepcopy
from itertools import combinations


class Matrix:

    def __init__(self, m):
        self._m = m
        self.width = len(m[0])
        self.height = len(m)

    def get(self, x, y):
        return self._m[y][x]

    def set(self, x, y, v):
        self._m[y][x] = v

    def is_valid(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        else:
            return True

    def indices(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self._m)


class LabSimulator(Matrix):
    EMPTY = 0
    WALL = 1
    VIRUS = 2

    def __init__(self, m):
        self.initial = deepcopy(m)
        super().__init__(m)

    def _initiate(self):
        for y in range(self.height):
            for x in range(self.width):
                self._m[y][x] = self.initial[y][x]

    def _spread(self):

        def adjacent(x, y):
            indices = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            return (p for p in indices if self.is_valid(*p))

        for p in self.indices():
            if self.get(*p) != self.VIRUS:
                continue
            stack = list(adjacent(*p))
            while stack:
                p = stack.pop()
                if self.get(*p) == self.EMPTY:
                    stack += adjacent(*p)
                    self.set(*p, self.VIRUS)

    def _empty_indices(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x, y) == self.EMPTY:
                    yield (x, y)

    def simulate_wall(self):

        def count_empty():
            empty = 0
            for p in self.indices():
                if self.get(*p) == self.EMPTY:
                    empty += 1
            return empty

        max_safezone = 0
        for spots in combinations(self._empty_indices(), 3):
            for p in spots:
                self.set(*p, self.WALL)
            self._spread()
            if (cnt := count_empty()) > max_safezone:
                max_safezone = cnt
                self.maxspots = spots
            self._initiate()

        return max_safezone
            

if __name__ == "__main__":
    readl = sys.stdin.readline
    h, w = map(int, readl().split())
    lab = [[int(c) for c in readl().split()] for _ in range(h)]
    simul = LabSimulator(lab)
    print(simul.simulate_wall())
