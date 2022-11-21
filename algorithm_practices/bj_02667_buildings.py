'''
BAEKJOON 2667번 문제
https://www.acmicpc.net/problem/2667
[ 입력 ]
1) N 2) N개의 줄에 각 줄의 데이터 (정사각형)
[ 출력 ]
1) 총 단지의 수
2) 각 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩.
'''
import sys

class StringMatrix:
def __init__(self, m):
    self._m = m
    self.size = len(m)

def get(self, x, y):
    if x < 0 or y < 0:
        raise IndexError
    return self._m[y][x]

def gen_indices(self):
    for y in range(self.size):
        yield from [(x, y) for x in range(self.size)]


def find_groups(m):
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited = set()
subdivisions = []

def cond(p):
    return (p not in visited) and (m.get(*p) == "1")

for x, y in filter(cond, m.gen_indices()):
    stack = [(x, y)]
    number = 0
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        try:
            v = m.get(x, y)
        except IndexError:
            continue
        if v == "1":
            visited.add((x, y))
            number += 1
            stack += ((x+dx, y+dy) for dx, dy in dirs)

    subdivisions.append(number)

subdivisions.sort()

# Print Answer
print(len(subdivisions))
for n in subdivisions:
    print(n)
            

if __name__ == "__main__":
readl = sys.stdin.readline
n = int(readl())
m = StringMatrix([readl() for _ in range(n)])
find_groups(m)
