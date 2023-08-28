"""
BAEKJOON 1697번 문제
https://www.acmicpc.net/problem/1697
걸으면 +1 또는 -1, 순간이동하면 *2
Node당 3개의 children이 있는 tree를 BFS한다고 생각하고 풀 예정이다.
[ 입력 ]
N: 수빈의 위치 (시작위치) K: 동생의 위치 (목적지)
[ 출력 ]
동생을 찾는 가장 빠른 시간.
"""
import sys


def solution(s, e):
    # Initialization
    move = 0
    visited = set()
    curr_set = {s}
    next_set = set()

    # Helper function
    def cond(x):
        return (x >= 0) and ((x - e + move <= abs(e - s)) if x > e else True)

    # BFS until finding endpoint
    while move < abs(s - e):
        for x in filter(cond, curr_set):
            if x == e:
                return move
            visited.add(x)
            next_set |= {x - 1, x + 1, 2 * x} - visited
        curr_set = next_set
        next_set = set()
        move += 1

    return move


if __name__ == "__main__":
    readln = sys.stdin.readline
    n, k = map(int, readln().split())
    print(solution(n, k))
