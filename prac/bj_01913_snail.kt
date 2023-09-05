/* https://www.acmicpc.net/problem/1913 */

fun main() {
    val snail = Snail(readLine()!!.toInt(), readLine()!!.toInt())
    snail.fill()
    println(snail.arr.map { it.joinToString(" ") }.joinToString("\n"))
    println("${snail.x + 1} ${snail.y + 1}")
}

class Snail(n: Int, target: Int) {
    val maxVal = n * n
    val start = n / 2
    val target = target
    var arr = Array<Array<Int>>(n) { Array<Int>(n) { 0 } }
    var x = 0
    var y = 0

    val U = Pair(-1, 0)
    val R = Pair(0, 1)
    val D = Pair(1, 0)
    val L = Pair(0, -1)

    fun fill() {
        var (i, j) = Pair(start, start)
        var (mvCnt, maxMv) = Pair(0, 1)
        var dir = U

        for (v in 1..maxVal) {
            arr[i][j] = v

            if (v == target) {
                x = i
                y = j
            }

            if (mvCnt == maxMv) {
                dir = nextDir(dir)
                mvCnt = 1
                if (dir == U || dir == D) {
                    maxMv += 1
                }
            } else {
                mvCnt += 1
            }
            i += dir.first
            j += dir.second
        }
    }

    fun nextDir(dir: Pair<Int, Int>): Pair<Int, Int> = when (dir) {
        U -> R
        R -> D
        D -> L
        L -> U
        else -> U
    }
}
