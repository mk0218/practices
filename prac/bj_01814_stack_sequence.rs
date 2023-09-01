/* https://www.acmicpc.net/problem/1874 */
use std::io::stdin;

fn main() {
    let n = read_i32();
    println!("{}", sol(n))
}

fn sol(n: i32) -> String {
    let mut stack = Stack::new();
    let mut cnt = 1..=n;

    for _ in 0..n {
        let x: i32 = read_i32();
        loop {
            if let Some(v) = stack.top() {
                if v > x {
                    return String::from("NO");
                } else if v == x {
                    break;
                };
            };
            stack.push(cnt.next().unwrap());
        }
        stack.pop();
    }
    return stack.ops;
}

fn read_i32() -> i32 {
    let mut buf = String::new();
    match stdin().read_line(&mut buf) {
        Ok(_) => return buf.trim().parse().unwrap(),
        Err(why) => panic!("{}", why),
    }
}

const STACK_MAX_SIZE: usize = 100_000;

struct Stack {
    arr: [i32; STACK_MAX_SIZE],
    size: usize,
    ops: String,
}

impl Stack {
    fn new() -> Stack {
        return Stack {
            arr: [0; STACK_MAX_SIZE],
            size: 0,
            ops: String::new(),
        };
    }

    fn push(&mut self, x: i32) {
        self.arr[self.size] = x;
        self.ops += "+\n";
        self.size += 1;
    }

    fn pop(&mut self) -> Option<i32> {
        if self.size > 0 {
            self.size -= 1;
            self.ops += "-\n";
            Some(self.arr[self.size])
        } else {
            None
        }
    }

    fn top(&self) -> Option<i32> {
        if self.size > 0 {
            Some(self.arr[self.size - 1])
        } else {
            None
        }
    }
}
