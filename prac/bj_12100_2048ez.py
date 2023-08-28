"""
BAEKJOON 12100번 문제
https://www.acmicpc.net/problem/12100
[ 입력 ]
첫째 줄: 보드의 크기 N (1 ≤ N ≤ 20)
둘째 줄부터 N개의 줄: 게임판의 초기 상태. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.
[ 출력 ]
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력하라
"""
import sys
from itertools import chain
from enum import Enum, auto


class DirType(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    FORWARD = auto()
    BACKWARD = auto()


class GameMove(Enum):
    L = (-1, 0)
    R = (1, 0)
    U = (0, -1)
    D = (0, 1)

    @property
    def iter_increment(self):
        return (-n for n in self.value)

    @property
    def type(self):
        if self in (GameMove.L, GameMove.R):
            return DirType.HORIZONTAL
        else:  # GameMove.U | GameMove.D
            return DirType.VERTICAL

    @property
    def incr_or_decr(self):
        if self in (GameMove.R, GameMove.D):
            return DirType.FORWARD
        else:  # GameMove.L | GameMove.U
            return DirType.BACKWARD


class SquareMatrix:
    def __init__(self, matrix):
        self._m = matrix
        self.size = len(matrix)

    def get(self, x, y):
        return self._m[y][x]

    def set(self, x, y, v):
        self._m[y][x] = v

    def max(self):
        return max(chain(*self._m))

    def __eq__(self, other):
        return True if self._m == other._m else False

    def __repr__(self):
        return str(self._m)

    def __str__(self):
        return "\n".join((" ".join(map(str, row)) for row in self._m))


class GameBoard(SquareMatrix):
    def __init__(self, initial_board):
        super().__init__(initial_board)

    def copy(self):
        m = [row[:] for row in self._m]
        return GameBoard(m)

    def iter_order(self, dir: GameMove):
        """Generates an iterator by dir"""

        def sort(i, j):
            return (i, j) if dir.type == DirType.HORIZONTAL else (j, i)

        def order(indices):
            return (
                indices if dir.incr_or_decr == DirType.BACKWARD else reversed(indices)
            )

        indices = range(self.size)
        for j in indices:
            yield (sort(i, j) for i in order(indices))

    def next(self, dir: GameMove):
        board = self.copy()
        dx, dy = dir.iter_increment
        it = board.iter_order(dir)
        for row in it:
            for i, (x, y) in enumerate(row):
                value = board.get(x, y)
                # first element
                if i == 0:
                    m, n, v = x, y, value
                    continue
                # empty square
                if not value:
                    continue
                # same as previous value => merge
                if value == v:
                    board.set(m, n, v * 2)
                    board.set(x, y, 0)
                    m, n, v = m + dx, n + dy, 0
                # not empty, but different to previous value
                elif value != 0:
                    if v != 0:
                        m, n = m + dx, n + dy
                    v = value
                    if (m, n) == (x, y):
                        continue
                    board.set(m, n, value)
                    board.set(x, y, 0)
        return board


def solution(board):
    """A DFS-way solution using recursion"""

    def game_simulate(board, count):
        if count == 5:
            return board.max()
        max_block = board.max()
        for dir in GameMove:
            if (next_state := board.next(dir)) != board:
                max_block = max(max_block, game_simulate(next_state, count + 1))
        return max_block

    initial_game = GameBoard(board)
    return game_simulate(initial_game, 0)


if __name__ == "__main__":
    readl = sys.stdin.readline
    n = int(readl())
    board = [list(map(int, readl().split())) for _ in range(n)]
    print(solution(board))
