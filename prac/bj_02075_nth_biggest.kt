/* https://www.acmicpc.net/problem/2075 */
import kotlin.math.min

fun main() {
    val n = readLine()!!.toInt()
    val arr = DescArr(n)
    var numbers = List<List<Int>>(n) { readLine()!!.split(" ").map { it.toInt() }}
    numbers.asReversed().forEach { it.forEach { v: Int -> arr.push(v) }}
    println(arr.arr[n - 1])
}

class DescArr(maxSize: Int) {
    val maxSize = maxSize
    var arr = IntArray(maxSize + 1) { -1000000001 }
    var size = 0

    fun push(v: Int) {
        if (arr[maxSize - 1] <= v) {
            var idx = size
            while (idx > 0 && v > arr[idx - 1]) {
                arr[idx] = arr[--idx]
            }
            arr[idx] = v
            size = min(size + 1, maxSize - 1)
        }
    }
}
