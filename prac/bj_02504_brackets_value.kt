/* https://www.acmicpc.net/problem/2504 */

fun main() {
    val str = readLine()!!
    println(sol(str))
}

fun sol(str: String): Int {
    val stack = Stack(30)
    var buffer = IntArray(30) { 0 }
    var i = 0
    var prev = ' '

    for (c in str) {
        when (c) {
            ')' -> {
                if (stack.pop() == '(') {
                    buffer[stack.size] += if (buffer[stack.size + 1] == 0) 2 else {
                        2 * buffer[stack.size + 1]
                    }
                    buffer[stack.size + 1] = 0
                } else return 0
            }
            ']' -> {
                if (stack.pop() == '[') {
                    buffer[stack.size] += if (buffer[stack.size + 1] == 0) 3 else {
                        3 * buffer[stack.size + 1]
                    }
                    buffer[stack.size + 1] = 0
                } else return 0

            }
            else -> stack.push(c)
        }
    }

    return buffer[0]
}

class Stack(maxSize: Int) {
    val arr = Array<Char?>(maxSize) { null }
    var size = 0
    val push = { c: Char -> arr[size++] = c; this }
    val pop: () -> Char? = { if (size > 0) arr[--size] else null }
    val head: () -> Char? = { if (size > 0) arr[size - 1] else null }
}
