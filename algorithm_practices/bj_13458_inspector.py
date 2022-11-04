'''
BAEKJOON 13458번 문제
https://www.acmicpc.net/problem/13458
'''
import sys
from math import ceil

if __name__ == '__main__':
    readl = sys.stdin.readline
    n = int(readl())
    a = list(map(int, readl().split()))
    b, c = map(int, readl().split())
    need = [0] * len(a)
    for i, ai in enumerate(a):
        need[i] += 1
        ai -= b
        if ai > 0:
            need_more = ceil(ai / c)
            need[i] += need_more
    print(sum(need))