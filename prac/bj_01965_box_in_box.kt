/* https://www.acmicpc.net/problem/1965 */

import kotlin.math.max

fun main() {
    val n = readLine()!!.toInt()
    val boxes = readLine()!!.split(" ").map { it.toInt() }
    var maxPut = IntArray(n) { 0 }

    for ((i, box) in boxes.withIndex()) {
        maxPut[i] = 1
        for (j in 0..(i-1)) {
            if (boxes[j] < box) {
                maxPut[i] = max(maxPut[i], maxPut[j] + 1)
            }
        }
    }

    println(maxPut.maxOrNull()!!)
}