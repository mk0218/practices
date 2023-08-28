"""
BAEKJOON 5014번 문제
https://www.acmicpc.net/problem/5014
s에서 g까지 가야 한다.
[ 입력 ]
f s g u d
f: # of floors, s: current floor, g: destination
u, d: 버튼 누를 때 한번에 움직이는 층 수
[ 출력 ]
버튼 눌러야 하는 최소 횟수
"""
import sys


def solve(f, s, g, u, d):
    clicks = 0
    current = {s}
    visited = set()

    def cond(x):
        return x not in visited and x >= 1 and x <= f

    def next_floors(c):
        return filter(cond, (c + u, c - d))

    # BFS until finding g or all floors are visited.
    while clicks <= f:
        nextset = set()
        for c in current:
            if c == g:
                return clicks
            for nf in next_floors(c):
                nextset.add(nf)
                visited.add(nf)
        if not nextset:
            return "use the stairs"

        current = nextset
        clicks += 1

    return clicks


if __name__ == "__main__":
    f, s, g, u, d = map(int, sys.stdin.readline().split())
    print(solve(f, s, g, u, d))
