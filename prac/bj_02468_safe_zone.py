"""
https://www.acmicpc.net/problem/2468
"""
import sys


def sol(m, min_h, max_h) -> int:
    n, level = len(m), min_h - 1
    safe_zones, visited = [], [[-1 for _ in range(n)] for _ in range(n)]

    def count_safe_zone() -> int:
        count = 0
        for j in range(n):
            for i in range(n):
                count += dfs(i, j)
        return count
    
    def dfs(x: int, y: int) -> int:
        to_visit = [(x, y)]
        area = 0
        while to_visit:
            i, j = to_visit.pop()
            if (i >= 0 and j >= 0 and i < n and j < n
                and visited[j][i] != level
                and m[j][i] > level):
                visited[j][i] = level
                area += 1
                to_visit += [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                    ]
        if area > 0:
            return 1
        else:
            return 0

    while level <= max_h:
        safe_zones.append(count_safe_zone())
        level += 1

    return max(safe_zones)


if __name__ == "__main__":
    readline = sys.stdin.readline
    n, m = int(readline()), []
    min_h, max_h = 100, 1

    for _ in range(n):
        row = list(map(int, readline().split()))
        min_h, max_h = min(min_h, min(row)), max(max_h, max(row))
        m.append(row)

    print(sol(m, min_h, max_h))