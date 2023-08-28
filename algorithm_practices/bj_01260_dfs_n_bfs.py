"""
BAEKJOON 1260번 문제
https://www.acmicpc.net/problem/1260
[ 입력 ]
정점의 개수 N (<=1000), 간선의 개수 M (<= 10000), 탐색을 시작할 정점의 번호 V
M개의 줄에 간선이 연결하는 두 정점의 번호
[ 출력 ]
첫째 줄에는 DFS 탐색순서
둘째 줄에는 BFS 탐색순서
"""
import sys


def dfs(s, edges):
    visited = []

    def recursive_dfs(v):
        if v in visited:
            return
        visited.append(v)
        for w in edges[v]:
            recursive_dfs(w)

    recursive_dfs(s)
    return " ".join(map(str, visited))


def dfs_no_recursion(s, edges):
    visited = []
    stack = [s]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.append(v)
        stack.extend(reversed(edges[v]))
    return " ".join(map(str, visited))


def bfs(s, edges):
    visited = [s]
    current = edges[s]
    while current:
        next = []
        for w in current:
            if w not in visited:
                visited.append(w)
                next.extend(edges[w])
        current = next
    return " ".join(map(str, visited))


def solve(s, edges):
    # print(dfs(s, edges))
    print(dfs_no_recursion(s, edges))
    print(bfs(s, edges))


if __name__ == "__main__":
    readl = sys.stdin.readline
    n, m, v = map(int, readl().split())
    edges = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, w = map(int, readl().split())
        edges[u].append(w)
        edges[w].append(u)
    for e in edges.values():
        e.sort()
    solve(v, edges)
