"""
BAEKJOON 4673번 문제
https://www.acmicpc.net/problem/4673
이게 뭐꼬
소수 구할때 쓰는 어쩌구 그리스사람의 체 방법으로 풀어볼까
d(n): n과 n의 각 자리수를 더하는 함수
이 때 n을 d(n)의 생성자라고 하고 생성자가 없는 숫자를 셀프 넘버라고 한다
[ 출력 ]
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하세요
"""


def d(n):
    def add(n):
        if n == 0:
            return 0
        return add(n // 10) + n % 10

    return add(n) + n


def solve():
    not_self_number = set()
    for n in range(1, 10001):
        if n in not_self_number:
            continue
        print(n)
        while n <= 10000:
            n = d(n)
            not_self_number.add(n)


if __name__ == "__main__":
    solve()
