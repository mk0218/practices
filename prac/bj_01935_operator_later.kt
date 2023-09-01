/* https://www.acmicpc.net/problem/1935 */


fun main() {
    val n = readLine()!!.toInt()
    val exp = readLine()!!
    val operands = DoubleArray(n) { readLine()!!.toDouble() }
    val stack = Stack(100)

    for (c in exp) {
        when (c) {
            '+', '-', '*', '/' -> {
                val b: Double = stack.pop()
                val a: Double = stack.pop()
                stack.push(when (c) {
                    '+' -> a + b
                    '-' -> a - b
                    '*' -> a * b
                    else -> a / b   // '/'
                })
            }
            else -> stack.push(operands[indexOf(c)])
        }
    }
    println("%.2f".format(stack.pop()))
}

inline fun indexOf(c: Char): Int = c.code - 'A'.code

class Stack(maxSize: Int) {
    val arr = DoubleArray(maxSize)
    var size = 0
    fun push(x: Double) { arr[size++] = x }
    fun pop(): Double { return arr[--size] }
}
