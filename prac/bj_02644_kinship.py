"""
BAEKJOON 2644번 문제
https://www.acmicpc.net/problem/2644
아 이문제는 제목만 딱 봐도 tree가 나오죠? tree 아니면 개족보임
[ 입력 ]
(1) n: 전체 사람의 수, (2) a b: 촌수를 계산할 두 사람
(3) m: 부모 자식 관계의 수 (4) x y: x가 부모 y가 자식 (m줄)
부모는 최대 한 명만 주어짐
[ 출력 ]
촌수. 친척이 아닐 때에는 -1
"""
import sys


class Person:
    def __init__(self, n):
        self.n = n
        self.parent = None
        self.children = []

    @property
    def family(self):
        if self.parent:
            yield self.parent
        yield from self.children

    def __repr__(self):
        return f"#{self.n}: parent - {self.parent}, children - {self.children}"


def solve(a, b, relations):
    dist, current = 1, [a]
    visited = set()
    while current:
        next_pp = []
        for n in current:
            visited.add(n)
            for person in filter(lambda n: n not in visited, relations[n].family):
                if person == b:
                    return dist
                next_pp.append(person)
        current = next_pp
        dist += 1
    return -1


if __name__ == "__main__":
    readl = sys.stdin.readline
    n = int(readl())
    a, b = map(int, readl().split())
    m = int(readl())
    relations = {}
    for _ in range(m):
        x, y = map(int, readl().split())
        relations.setdefault(x, Person(x)).children.append(y)
        relations.setdefault(y, Person(y)).parent = x

    print(solve(a, b, relations))
