"""
BAEKJOON 13460번 문제
https://www.acmicpc.net/problem/13460
"""
import sys
from enum import Enum
from typing import Generator, Iterator, Tuple


class MarbleExit(Exception):
    pass


class RedMarbleExit(MarbleExit):
    pass


class BlueMarbleExit(MarbleExit):
    pass


class Dir(Enum):
    U = (0, -1)
    D = (0, 1)
    L = (-1, 0)
    R = (1, 0)

    @staticmethod
    def next_move(dir: str):
        if Dir[dir] in (Dir.U, Dir.D):
            return (Dir.L, Dir.R)
        elif Dir[dir] in (Dir.L, Dir.R):
            return (Dir.U, Dir.D)


class Matrix:
    def __init__(self, it: Generator[Iterator[str], None, None]):
        self._m = [[c for c in subit] for subit in it]
        self._w = len(self._m[0])
        self._h = len(self._m)

    def get(self, x, y):
        return self._m[y][x]

    def set(self, x, y, v):
        self._m[y][x] = v

    def __str__(self):
        return "\n".join(("".join(row) for row in self._m))


class MarblesBoard(Matrix):
    RED = "R"
    BLUE = "B"
    HOLE = "O"
    WALL = "#"
    EMPTY = "."

    def __init__(self, board: Generator[Iterator[str], None, None]):
        super().__init__(board)

        def find():
            hole = (red := (blue := ()))
            for i, row in enumerate(self._m):
                for j, c in enumerate(row):
                    if not hole and (c == self.HOLE):
                        hole = (j, i)
                    if not blue and (c == self.BLUE):
                        blue = (j, i)
                    if not red and (c == self.RED):
                        red = (j, i)
                    if hole and blue and red:
                        return (hole, blue, red)
            raise Exception(
                f"hole: {hole}, blue: {blue}, red: {red}\n"
                f"matrix:\n{self._m.__str__()}"
            )

        self._xy_hole, self._xy_blue, self._xy_red = find()
        self._move_cnt = 0
        self._leftmost, self._rightmost = 1, self._w - 2
        self._top, self._bottom = 1, self._h - 2

    def set_marbles(self, *, blue=None, red=None):
        if blue and self.is_valid_position(*blue):
            self.set(*self._xy_blue, self.EMPTY)
            self._xy_blue = tuple(blue)
            self.set(*self._xy_blue, self.BLUE)
        if red and self.is_valid_position(*red):
            self.set(*self._xy_red, self.EMPTY)
            self._xy_red = tuple(red)
            self.set(*self._xy_red, self.RED)

    def is_valid_position(self, x, y):
        return (
            (x >= self._leftmost and x <= self._rightmost)
            and (y >= self._top and y <= self._bottom)
            and self.get(x, y) != self.WALL
        )

    def move_simulate(self, dir: Dir) -> Generator[Tuple[int, int], None, None]:
        """
        현재상태에서 dir 방향으로 구슬들을 움직이면 어떻게 될지 simulation하는 함수
        output: ((파란 구슬 위치), (빨간 구슬 위치))의 Generator
        exception: RedMarbleExit(성공) 또는 BlueMarbleExit(실패)
        """
        xo, yo = self._xy_hole
        dx, dy = dir.value
        marble = {  # [x, y, stuck, exit]
            self.BLUE: [*self._xy_blue, False, False],
            self.RED: [*self._xy_red, False, False],
        }

        def both_stuck():
            return marble[self.BLUE][2] and marble[self.RED][2]

        def blue_exit():
            return marble[self.BLUE][3]

        def red_exit():
            return marble[self.RED][3]

        # 한 칸씩 움직이기
        while not both_stuck() and not blue_exit():
            for key, [x, y, stuck, exit] in marble.items():
                if stuck:
                    continue
                x, y = x + dx, y + dy
                if self.is_valid_position(x, y):
                    marble[key][:2] = x, y
                else:
                    marble[key][2] = True
                if (x, y) == (xo, yo):
                    marble[key][2] = True
                    marble[key][3] = True

            # 두 구슬이 같은 칸에 있게 되면 나중에 온 구슬을 원래 위치로 되돌린다.
            # 또한 이런경우에는 두 구슬 모두 더이상 움직일 수 없으므로 stuck 처리.
            if not (blue_exit() or red_exit()):
                if marble[self.BLUE][:2] == marble[self.RED][:2]:
                    for key, [x, y, stuck, _] in marble.items():
                        if not stuck:
                            marble[key][:2] = x - dx, y - dy
                            marble[key][2] = True
                            break
        if blue_exit():
            raise BlueMarbleExit  # 실패
        elif red_exit():
            raise RedMarbleExit  # 성공
        return (tuple(seq[:2]) for seq in marble.values())

    def move(self, dir: Dir):  # 안필요한데 테스트 수정 안하려고 일단 추가해둠
        blue, red = self.move_simulate(dir)
        self.set_marbles(blue=blue, red=red)

    def search_routes(self) -> int:
        """빨강이가 들어가야 한다아"""
        visited = {(self._xy_blue, self._xy_red)}
        routes = {}
        for dir in Dir:
            try:
                blue, red = self.move_simulate(dir)
            except BlueMarbleExit:
                continue
            except RedMarbleExit:
                return dir.name
            if (blue, red) not in visited:
                routes.setdefault(dir.name, (blue, red))
                visited.add((blue, red))
        # routes => {'U': ((-, -), (-, -)), 'D': ..., 'L': ..., 'R': ...}

        while routes:
            routes_next = {}
            for route, (blue, red) in routes.items():
                visited.add((self._xy_blue, self._xy_red))
                self.set_marbles(blue=blue, red=red)

                for dir in Dir.next_move(route[-1]):
                    try:
                        blue, red = self.move_simulate(dir)
                    except BlueMarbleExit:
                        continue
                    except RedMarbleExit:
                        return route + dir.name
                    if (blue, red) not in visited:
                        routes_next.setdefault(route + dir.name, (blue, red))
                        visited.add((blue, red))
            routes = routes_next
        return ""


def gen_matrix(width, height):
    for _ in range(height):
        yield iter(sys.stdin.readline()[:width])


if __name__ == "__main__":
    height, width = map(int, sys.stdin.readline().split())
    board = MarblesBoard(gen_matrix(width, height))
    route = board.search_routes()
    if (not route) or ((ans := len(route)) > 10):
        print(-1)
    else:
        print(ans)
