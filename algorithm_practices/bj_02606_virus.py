"""
BAEKJOON 2606번 문제
https://www.acmicpc.net/problem/2606
[ 입력 ]
첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
[ 출력 ]
1번 컴퓨터가 웜 바이러스에 걸렸을 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
"""
import sys


def solve(edges):
    visited = set()
    stack = [1]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        stack += edges[v]
    print(len(visited) - 1)


if __name__ == "__main__":
    readl = sys.stdin.readline
    n = int(readl())
    m = int(readl())
    edges = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        v, w = map(int, readl().split())
        edges[v].append(w)
        edges[w].append(v)

    solve(edges)
