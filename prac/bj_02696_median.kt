/* https://www.acmicpc.net/problem/2696 */

import kotlin.math.min

fun main() {
    for (tc in 1..readLine()!!.toInt()) {
        val n = readLine()!!.toInt()
        val values = mutableListOf<Int>()
        for (i in 1 .. n / 10 + 1) {
            values += readLine()!!.split(" ").map { it.toInt() }
        }

        val m = (n + 1) / 2
        val seq = SortedSequence()
        val median = mutableListOf<Int>()

        for ((i, v) in values.withIndex()) {
            seq.push(v)
            if (i % 2 == 0) {
                median.add(seq.median())
            }
        }
        println(m)
        for (i in 0 .. m / 10) {
            println(median.slice(10 * i .. min(10 * (i + 1), median.size) - 1)
                          .joinToString(" "))
        }
    }
}

class SortedSequence() {
    val seq = mutableListOf<Int>()

    fun center(s: Int, e: Int): Int = (s + e) / 2
    fun median(): Int = seq[center(0, seq.size - 1)]

    fun push(v: Int) {
        fun findIndex(s: Int, e: Int): Int {    // BinSearch
            if (v <= seq[s]) return s
            if (v > seq[e]) return e + 1
            if (e - s == 1) return e
            val idx = center(s, e)
            return if (v < seq[idx]) findIndex(s, idx)
            else if (v > seq[idx]) findIndex(idx, e)
            else idx
        }
        if (seq.size == 0) seq.add(v)
        else seq.add(findIndex(0, seq.size - 1), v)
    }
}
