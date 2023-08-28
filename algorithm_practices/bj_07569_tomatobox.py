"""
BAEKJOON 7569번 문제
https://www.acmicpc.net/problem/7569
1: 익은토마토
0: 안 익은 토마토
-1: 토마토 없음
기준대로 BFS해서 몇 단계에서 끝나는지를 보면 된다.
[ 입력 ]
M(width), N(? 영어실력 이슈), H(height)
N개의 줄에 각각 M개의 값
이게 H번
[ 출력 ]
토마토가 모두 익을 때까지 며칠이 걸릴까용
(처음부터 끝나있으면 0, 모두 익을 수 없으면 -1)
"""
import sys
from enum import IntEnum


class ThreeDimArr:
    def __init__(self, m):
        self._m = m
        self.xsize = len(m[0][0])
        self.ysize = len(m[0])
        self.zsize = len(m)

    def get(self, x, y, z):
        return self._m[z][y][x]

    def set(self, x, y, z, value):
        self._m[z][y][x] = value

    def adjacent(self, x, y, z):
        def valid(p):
            x, y, z = p
            return (
                (x >= 0 and x < self.xsize)
                and (y >= 0 and y < self.ysize)
                and (z >= 0 and z < self.zsize)
            )

        return filter(
            valid,
            (
                (x - 1, y, z),
                (x + 1, y, z),
                (x, y - 1, z),
                (x, y + 1, z),
                (x, y, z - 1),
                (x, y, z + 1),
            ),
        )

    def __str__(self):
        return "\n\n".join(
            ("\n".join(" ".join(map(str, row)) for row in floor) for floor in self._m)
        )


class TomatoStatus(IntEnum):
    GREEN = 0
    RED = 1
    NONE = -1


class TomatoBox(ThreeDimArr):
    def __init__(self, box):
        super().__init__(box)
        self.red = set()
        self.green = set()
        for z in range(self.zsize):
            for y in range(self.ysize):
                for x in range(self.xsize):
                    if (status := self.get(x, y, z)) == TomatoStatus.RED:
                        self.red.add((x, y, z))
                    elif status == TomatoStatus.GREEN:
                        self.green.add((x, y, z))


def solve_bfs(box) -> int:
    box = TomatoBox(box)
    day = -1
    current = list(box.red)
    next_ = []
    visited = set(current)

    while current:
        for tomato in current:
            for adjacent in filter(lambda p: p not in visited, box.adjacent(*tomato)):
                if box.get(*adjacent) == TomatoStatus.GREEN:
                    next_.append(adjacent)
                    visited.add(adjacent)
        current, next_ = next_, []
        day += 1

    if len(box.green - visited) == 0:
        return day
    else:
        return -1


if __name__ == "__main__":
    readl = sys.stdin.readline
    m, n, h = map(int, readl().split())
    box = []
    for _ in range(h):
        box.append([list(map(int, readl().split())) for _ in range(n)])
    print(solve_bfs(box))
