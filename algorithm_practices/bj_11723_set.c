#include <stdio.h>
/*
BAEKJOON 11723번 문제
https://www.acmicpc.net/problem/11723
C로 다시구현
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
 */

typedef enum Command {
    ADD = 31,
    REMOVE = 32,
    CHECK = 33,
    TOGGLE = 34,
    ALL = 35,
    EMPTY = 36,
} cmd;


typedef struct FakeSet {
    int exists[20];
} set;


void set_add (set *s, int x) {
    s -> exists[x-1] = 1;
}


void set_remove (set *s, int x) {
    s -> exists[x-1] = 0;
}


void set_check (set *s, int x) {
    printf("%d\n", s -> exists[x-1]);
}


void set_toggle (set *s, int x) {
    s -> exists[x-1] = !(s -> exists[x-1]);
}


void set_all (set *s) {
    for (int i = 0; i < 20; i++) {
        s -> exists[i] = 1;
    }
}


void set_empty (set *s) {
    for (int i = 0; i < 20; i++) {
        s -> exists[i] = 0;
    }
}


cmd get_cmd () {
    char command[9];
    scanf("%s", command) == 1;
    switch (command[0]) {
        case 'r': return REMOVE;
        case 'c': return CHECK;
        case 't': return TOGGLE;
        case 'e': return EMPTY;
        case 'a':
        default:
            if (command[1] == 'd') return ADD;
            else return ALL;
    }
}


void execute (set *s, cmd c) {
    int x;
    if (c != ALL && c != EMPTY) {
        scanf("%d", &x) == 1;
    }
    switch (c) {
        case (ADD):
            set_add(s, x); break;
        case (REMOVE):
            set_remove(s, x); break;
        case (CHECK):
            set_check(s, x); break;
        case (TOGGLE):
            set_toggle(s, x); break;
        case (ALL):
            set_all(s); break;
        case (EMPTY):
            set_empty(s); break;
    }
}


int main (void) {
    int n;
    cmd c;
    set s = {{}};

    if (scanf("%d", &n) != 1) {
        return 1;
    }
    
    for (int i = 0; i < n; i++) {
        execute(&s, get_cmd());
    }
    
    return 0;
}