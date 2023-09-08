/* https://www.acmicpc.net/problem/2696 */

import kotlin.math.min

inline fun avg(a: Int, b: Int): Int = (a + b) / 2

fun main() {
    for (tc in 1..readLine()!!.toInt()) {
        val n = readLine()!!.toInt()
        val values = mutableListOf<Int>()
        for (i in 1..n step 10) {
            values += readLine()!!.split(" ").map { it.toInt() }
        }

        val seq = SortedSequence()
        val median = mutableListOf<Int>()

        values.forEach {
            seq.push(it)
            if (seq.size % 2 == 1) {
                median.add(seq.median())
            }
        }
        
        println(median.size)

        for (i in 0 .. (median.size - 1) step 10) {
            println(median.slice(i .. min(i + 9, median.size - 1)).joinToString(" "))
        }
    }
}

class SortedSequence() {
    val seq = mutableListOf<Int>()
    val size get() = seq.size
    fun median(): Int = seq[avg(0, seq.size - 1)]
    fun push(v: Int) {
        fun findIndex(s: Int, e: Int): Int {    // BinSearch
            if (v <= seq[s]) return s
            if (v > seq[e]) return e + 1
            if (e - s == 1) return e
            val idx = avg(s, e)
            return if (v < seq[idx]) findIndex(s, idx)
            else if (v > seq[idx]) findIndex(idx, e)
            else idx
        }
        if (seq.size == 0) seq.add(v)
        else seq.add(findIndex(0, seq.size - 1), v)
    }
}
