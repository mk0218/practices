/* https://www.acmicpc.net/problem/1874 */

fun main() {
    val n = readLine()!!.toInt()
    val numbers = MutableList<Int>(n) { n - it }
    var stack = mutableListOf<Int>()
    var ops = mutableListOf<Char>()

    for (i in 1..n) {
        val m = readLine()!!.toInt()

        if (stack.isNotEmpty() && m < stack.last()) {
            println("NO")
            return
        }

        while (stack.isNullOrEmpty() || m > stack.last()) {
            stack.add(numbers.removeLastOrNull()!!)
            ops.add('+')
        }

        stack.removeLastOrNull()!!
        ops.add('-')
    }

    for (c in ops) {
        println(c)
    }
}
