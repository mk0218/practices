/* https://www.acmicpc.net/problem/2293 */

fun main() {
    val (n, k) = readLine()!!.split(" ").map { it.toInt() }
    var coins = IntArray(n) { readLine()!!.toInt() }
    var combs = Array(n) { IntArray(k + 1) { 0 } }

    for ((i, c) in coins.withIndex()) {
        for (v in 1..k) {
            if (v < c) {
                continue
            } else if (v == c) {
                combs[i][v] += 1
            } else {
                for (j in 0..i) {
                    combs[i][v] += combs[j][v-c]
                }
            }            

            println(combs.map { it.joinToString(" ") }.joinToString("\n"))
            println()
        }
    }

    println(combs.fold(0) { acc, arr -> acc + arr[k] })
}