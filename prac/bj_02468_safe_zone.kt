/* https://www.acmicpc.net/problem/2468 */

fun main() {
    println(SafeZone(Array<List<Int>>(readLine()!!.toInt()) {
        readLine()!!.split(" ").map { it.toInt() }
    }).simul())
}

class SafeZone(matrix: Array<List<Int>>) {
    val m = matrix
    val n = matrix.size

    val minHeight: Int
    val maxHeight: Int

    init {
        var (min, max) = Pair(m[0][0], m[0][0])
        for (row in m) {
            for (h in row) {
                if (h < min) {
                    min = h
                } else if (h > max) {
                    max = h
                }
            }
        }
        minHeight = min
        maxHeight = max
    }

    var safeZones = arrayListOf<Int>(1)
    var visited = Array<Array<Int>>(n) { Array<Int>(n) { -1 } }

    fun simul(): Int {
        for (level in (minHeight - 1) .. maxHeight) {
            val zones = simul_level(level)
            safeZones.add(zones)
        }
        return safeZones.sorted().lastOrNull()!!
    }

    fun simul_level(level: Int): Int {
        var zones = 0
        for (j in 0..(n-1)) {
            for (i in 0..(n-1)) {
                zones += visit(i, j, level)
            }
        }
        return zones
    }

    fun visit(i: Int, j: Int, level: Int): Int {
        if (i < 0 || j < 0 || i >= n || j >= n ||
            visited[j][i] == level || m[j][i] <= level) {
            return 0
        } else {
            visited[j][i] = level
            visit(i - 1, j, level)
            visit(i + 1, j, level)
            visit(i, j - 1, level)
            visit(i, j + 1, level)
            return 1
        }
    }
}