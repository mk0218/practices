/* https://www.acmicpc.net/problem/2075 */

fun main() {
    val n = readLine()!!.toInt()
    val arr = DescArr(n)
    var numbers = Array<IntArray>(n) { IntArray(n) { -1000000001 } }

    numbers.map {
        readLine()!!.split(" ").mapIndexed { i, v -> it[i] = v.toInt() }
    }

    for (j in n - 1 downTo 0) {
        for (i in (0..n - 1)) {
            arr.push(numbers[j][i])
        }
    }
    println(arr.stack.arr[n - 1])
}

class DescArr(maxSize: Int) {
    val maxSize = maxSize
    var stack = Stack(maxSize)
    var buffer = Stack(maxSize)
    
    fun push(v: Int): Boolean {
        if (stack.size == maxSize && stack.head() > v) {
            return false
        } else {
            while (stack.size > 0 && stack.head() < v) {
                buffer.push(stack.pop())
            }
            stack.push(v)
            while (stack.size < maxSize && buffer.size > 0) {
                stack.push(buffer.pop())
            }
            buffer.clear()
        }
        return true
    }
}

class Stack(maxSize: Int) {
    var size = 0
    var arr = IntArray(maxSize)
    val push = { v: Int -> arr[size++] = v }
    val pop = {  arr[--size] }
    val head = { arr[size - 1] }
    val clear = { size = 0 }
}