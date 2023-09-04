/* https://www.acmicpc.net/problem/2583 */

fun main() {
    val (m, n, k) = readLine()!!.split(" ").map { it.toInt() }
    val matrix = Matrix(n, m)
    
    for (square in 1..k) {
        val (x1, y1, x2, y2) = readLine()!!.split(" ").map { it.toInt() }
        for (j in y1 .. (y2 - 1)) {
            for (i in x1 .. (x2 - 1)) {
                matrix.setTrue(i, j)
            }
        }
    }

    var count = 0
    val areas = mutableListOf<Int>()

    for (j in 0 .. (matrix.height - 1)) {
        for (i in 0 .. (matrix.width - 1)) {
            val area = matrix.visit(i, j)
            if (area > 0) {
                count += 1
                areas.add(area)
            }
        }
    }

    println(count)
    println(areas.sorted().joinToString(" "))
}

class Matrix(width: Int, height: Int) {
    val width = width
    val height = height
    val arr = Array<Array<Boolean>>(height) { Array<Boolean>(width) { false }}
    val visited = mutableSetOf<Pair<Int, Int>>()

    fun get(i: Int, j: Int): Boolean = arr[j][i]
    fun setTrue(i: Int, j: Int) { arr[j][i] = true }

    fun visit(i: Int, j: Int): Int {
        if ( i < 0 ||  j < 0 || i >= width || j >= height ||
             Pair(i, j) in visited || get(i, j)) {
            return 0
        } else {
            visited.add(Pair(i, j))
            var area = 1
            area += visit(i - 1, j)
            area += visit(i + 1, j)
            area += visit(i, j - 1)
            area += visit(i, j + 1)
            return area
        }
    }
}