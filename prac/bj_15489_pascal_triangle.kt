/* https://www.acmicpc.net/problem/15489 */

fun main() {
    val (r, c, w) = readLine()!!.split(" ").map { it.toInt() }
    val triangle = arrayListOf(arrayOf(1))
    var sum = if (r == 1 && c == 1) 1 else 0

    for (i in 2..(r+w)) {
        var row = Array<Int>(i) { 0 }
        val prev = triangle.last()
        for (j in 0..(i-1)) {
            row[j] = prev.getOrElse(j-1) { 0 } + prev.getOrElse(j) { 0 }
            if (i >= r && i < (r + w) && j >= (c - 1) && j <= (c - 1 + i - r)) {
                sum += row[j]
            }
        }
        triangle.add(row)
    }
    
    println(sum)
}