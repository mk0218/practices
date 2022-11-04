'''
BAEKJOON 14499번 문제
https://www.acmicpc.net/problem/14499
'''
import sys
from enum import IntEnum


class Dir(IntEnum):
    E = 1
    W = 2
    N = 3
    S = 4


class Dice:

    def __init__(self):
        self._d = [0] * 6
        self._t = 1
        self._n = 2
        self._e = 3

    @property
    def t(self):
        return self._t

    @property
    def b(self):
        return (7 - self._t)

    @property
    def n(self):
        return self._n

    @property
    def e(self):
        return self._e

    @property
    def s(self):
        return (7 - self._n)

    @property
    def w(self):
        return (7 - self._e)

    def get_value(self, side_no):
        return self._d[side_no - 1]

    def set_bottom_value(self, value):
        self._d[self.b - 1] = value

    def roll(self, dir: Dir):
        if dir == Dir.N:
            self._t, self._n = self.s, self.t
        elif dir == Dir.S:
            self._t, self._n = self.n, self.b
        elif dir == Dir.E:
            self._t, self._e = self.w, self.t
        elif dir == Dir.W:
            self._t, self._e = self.e, self.b


def is_valid_move(n, m, x, y, dir: Dir):
    if dir == Dir.N and y == 0:
        return False
    elif dir == Dir.W and x == 0:
        return False
    elif dir == Dir.S and y == n - 1:
        return False
    elif dir == Dir.E and x == m - 1:
        return False
    return True


if __name__ == '__main__':
    readl = sys.stdin.readline
    n, m, y, x, k = map(int, readl().split())
    map_values = []
    for _ in range(n):
        map_values.append(list(map(int, readl().split())))
    cmds = map(int, readl().split())

    dice = Dice()

    for cmd in cmds:
        # 바깥으로 이동시키려고 하는 경우에는 무시한다.
        if not is_valid_move(n, m, x, y, cmd):
            # print(f'n: {n}, m: {m}, x: {x}, y: {y}, cmd: {cmd}')
            continue
        dice.roll(cmd)
        if cmd == Dir.N:
            y -= 1
        elif cmd == Dir.W:
            x -= 1
        elif cmd == Dir.S:
            y += 1
        elif cmd == Dir.E:
            x += 1
        if map_values[y][x] == 0:
            map_values[y][x] = dice.get_value(dice.b)
        else:
            dice.set_bottom_value(map_values[y][x])
            map_values[y][x] = 0
        print(dice.get_value(dice.t))
