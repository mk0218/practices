/* https://www.acmicpc.net/problem/1874 */

fun main() {
    val n = readLine()!!.toInt()
    sol(n)
}

fun sol(n: Int) {
    val stack = Stack()
    val numbers = generateSequence(1) { if (it < n) it + 1 else null }.iterator()

    for (i in 1..n) {
        val m = readLine()!!.toInt()

        while (m > stack.last() ?: 0) {
            stack.push(numbers.next())
        }
    
        if (m == stack.last()) {
            stack.pop()
        } else {
            println("NO")
            return
        }
    }

    for (c in stack.ops) {
        println(c)
    }
}

class Stack {
    val arr = arrayListOf<Int>()
    val ops = arrayListOf<Char>()

    fun push(x: Int) {
        arr.add(x)
        ops.add('+')
    }

    fun pop() {
        arr.removeLast()
        ops.add('-')
    }

    fun last(): Int? {
        return arr.lastOrNull()
    }
}

