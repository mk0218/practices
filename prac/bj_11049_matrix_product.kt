/* https://www.acmicpc.net/problem/11049 */

fun main() {
    val n = readLine()!!.toInt()
    val m = List(n) { readLine()!!.split(" ").map { it.toInt() } }
    val p = Array<IntArray>(n) { IntArray(n-it) { -1 } }

    for (i in 0..n-1) {
        p[0][i] = 0
    }

    for (k in 1..n-1) {
        for (i in 0..n-k-1) {
            val se = m[i][0] * m[i+k][1]
            for (j in i+1..i+k) {
                // println("k: $k, i: $i, j: $j")
                val v = p[j-i-1][i] + p[i+k-j][j] + se * m[j][0]
                // println("p[${j-i-1}][$i] + p[${i+k-j}][$j] + $se * m[$j][0]")
                // println("= ${p[j-i-1][i]} + ${p[i+k-j][j]} + $se * ${m[j][0]} = v")

                if (p[k][i] == -1 || v < p[k][i]) {
                    p[k][i] = v
                }
            }
        }
    }

    println(p[n-1][0])
}