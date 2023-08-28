"""
BAEKJOON 2178번 문제
https://www.acmicpc.net/problem/2178
1은 이동 가능, 0은 이동 불가능 칸
경로는 안 중요함 거리만 중요함
[ 입력 ]
N(width) M(height)
a M-length string consists of 0 and 1 for N lines
[ 출력 ]
지나야 하는 최소 칸의 수 (가능한 경우만 입력으로 주어짐)
"""
import sys


class Matrix:
    def __init__(self, m):
        self._m = m

    def get(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        return self._m[y][x]

    def __str__(self):
        return "\n".join(self._m)


def solve(height, width, maze):  # BFS
    NO = "0"
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    maze = Matrix(maze)
    dst = (width - 1, height - 1)

    visited = set()
    level, current = 1, {(0, 0)}

    while current:
        imonthenext_level = set()
        for x, y in current:
            try:
                go = maze.get(x, y)
            except IndexError:
                continue
            if (x, y) in visited or go == NO:
                continue
            if (x, y) == dst:
                return level
            visited.add((x, y))
            imonthenext_level |= {(x + dx, y + dy) for (dx, dy) in move}
        current = imonthenext_level
        level += 1


if __name__ == "__main__":
    readl = sys.stdin.readline
    height, width = map(int, readl().split())
    maze = [readl().rstrip() for _ in range(height)]
    print(solve(height, width, maze))
