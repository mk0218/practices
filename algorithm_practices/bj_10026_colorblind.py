'''
BAEKJOON 10026번 문제
https://www.acmicpc.net/problem/10026
[ 입력 ]
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.
[ 출력 ]
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
'''
import sys
from enum import Enum


class Color(str, Enum):
    R = "R"
    G = "G"
    B = "B"


class Picture:
    def __init__(self, m):
        self._m = m
        self.size = len(m)

    def get(self, x, y):
        return self._m[y][x]

    def is_valid(self, x, y):
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return False
        else:
            return True

    def change_color(self, src: Color, dst: Color):
        self._m[:] = [row.replace(src, dst) for row in self._m]
            
    
    def __str__(self):
        return "\n".join(self._m)


class PictureUtils:

    @staticmethod
    def traverse_same_color(pic: Picture, x, y):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        color = pic.get(x, y)
        visited = set()
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                if pic.is_valid(x+dx, y+dy) and pic.get(x+dx, y+dy) == color:
                    stack.append((x+dx, y+dy))
        return visited
        
    @staticmethod
    def count_region(pic: Picture):
        indices = ((x, y) for y in range(pic.size) for x in range(pic.size))
        visited, count = set(), 0
        for (x, y) in filter(lambda p: p not in visited, indices):
            visited |= PictureUtils.traverse_same_color(pic, x, y)
            count += 1
        return count


if __name__ == "__main__":
    readl = sys.stdin.readline
    n = int(readl())
    pic = Picture([readl().rstrip() for _ in range(n)])
    ans1 = PictureUtils.count_region(pic)
    pic.change_color(Color.R, Color.G)
    ans2 = PictureUtils.count_region(pic)
    print(f"{ans1} {ans2}")
    
