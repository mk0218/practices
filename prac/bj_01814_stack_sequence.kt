/* https://www.acmicpc.net/problem/1874 */


fun main() {
    val n = readLine()!!.toInt()
    println(sol(n))
}


fun sol(n: Int): String {
    val stk = Stack(n)
    var ops = StringBuilder()
    var k = 1
    for (i in 1..n) {
        val x = readLine()!!.toInt()
        while (x > stk.top() ?: 0) {
            ops.append("+\n")
            stk.push(k++)
        }
        if (x == stk.top()) {
            ops.append("-\n")
            stk.pop()
        } else {
            return "NO"
        }
    }
    return ops.toString()
}


class Stack(maxSize: Int) {
    val maxSize = maxSize
    val arr = IntArray(maxSize)
    var size = 0
    
    fun push(x: Int): Boolean {
        return if (size < maxSize) {
            arr[size++] = x
            true
        } else {
            false
        }
    }

    fun pop(): Int? {
        return if (size > 0) {
            arr[--size]
        } else {
            null
        }
    }

    fun top(): Int? {
        return if (size > 0) {
            arr[size - 1]
        } else {
            null
        }
    }

    fun empty(): Boolean {
        return (size == 0)
    }
}