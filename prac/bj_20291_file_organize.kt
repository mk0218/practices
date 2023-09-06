/* https://www.acmicpc.net/problem/20291 */

fun main() {
    val files = mutableMapOf<String, Int>()    // Key: format, Value: # of files
    for (i in 1 .. readLine()!!.toInt()) {
        val (_, format) = readLine()!!.split(".")
        files[format] = (files[format] ?: 0) + 1
    }
    println(files.map {
        val (k, v) = it
        "$k $v"
    }.sorted().joinToString("\n"))   
}