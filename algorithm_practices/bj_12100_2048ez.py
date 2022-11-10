'''
BAEKJOON 12100번 문제
https://www.acmicpc.net/problem/12100
[ 입력 ]
첫째 줄: 보드의 크기 N (1 ≤ N ≤ 20)
둘째 줄부터 N개의 줄: 게임판의 초기 상태. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.
[ 출력 ]
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력하라
'''
import sys
from enum import Enum, auto


class DirType(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()

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
        else:  # GameMove.U or GameMove.D
            return DirType.VERTICAL


class SquareMatrix:

    def __init__(self, matrix):
        self._m = matrix
        self.size = len(matrix)

    def get(x, y):
        return self._m[y][x]

    def set(x, y, v):
        self._m[y][x] = v

    def valid_index(index):
        if index < 0 or index >= self.size:
            return False
        else:
            return True


class GameBoard(SquareMatrix):

    def __init__(self, initial_board):
        super().__init__(initial_board)

    def iter_order(self, dir: GameMove):  # 안이쁜디
        index_range = range(self.size)

        if sum(dir.value) > 0:
            index_range = reversed(index_range)

        for j in index_range:
            if dir.type == DirType.HORIZONTAL:
                yield from ((i, j) for i in index_range)
            else:  # dir.type == DirType.VERTICAL
                yield from ((j, i) for i in index_range)  # 이 반복 어떻게 없앱니까
    
    def next(self, dir: GameMove):
        dx, dy = dir.value
        for x, y in self.iter_order(dir):
            if self.get(x, y) == 0:
                continue
            i, j = x, y
            while self.valid_index(i) and self.valid_index(j):
                pass
            


def solution(board):
    game0 = GameBoard(board)
    it = game0.iter_order(GameMove.D)
    for v in it:
        print(v)
    return 0


if __name__ == "__main__":
    readl = sys.stdin.readline
    n = int(readl())
    board = [map(int, readl().split()) for _ in range(n)]
    print(solution(board))
