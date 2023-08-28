"""
BAEKJOON 11723번 문제
https://www.acmicpc.net/problem/11723
근데 이거 파이썬으로 구현하는거 의미있나?
[ 구현 ]
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
[ 입력 ]
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
[ 출력 ]
check 연산이 주어질때마다, 결과를 출력한다.
"""
import sys


class Set:
    def __init__(self):
        self.s = set()

    def add(self, x):
        self.s.add(x)

    def remove(self, x):
        if x in self.s:
            self.s.remove(x)

    def check(self, x):
        if x in self.s:
            print("1")
        else:
            print("0")

    def toggle(self, x):
        if x in self.s:
            self.s.remove(x)
        else:
            self.s.add(x)

    def all(self):
        self.s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    def empty(self):
        self.s = set()


if __name__ == "__main__":
    readl = sys.stdin.readline
    n = int(readl())
    s = set()
    commands = (readl().split() for _ in range(n))
    for cmd in commands:
        if cmd[0] == "add":
            s.add(int(cmd[1]))
        elif cmd[0] == "remove":
            if (x := int(cmd[1])) in s:
                s.remove(x)
        elif cmd[0] == "check":
            if int(cmd[1]) in s:
                print("1")
            else:
                print("0")
        elif cmd[0] == "toggle":
            s = s ^ {int(cmd[1])}
        elif cmd[0] == "all":
            s = {i for i in range(1, 21)}
        elif cmd[0] == "empty":
            s = set()
