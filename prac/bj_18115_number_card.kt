/* https://www.acmicpc.net/problem/18115 */

fun sol(skill: List<Int>) {
    val cards = ArrayDeque<Int>(skill.size)    // 0이 위, 끝이 아래
    for ((i, s) in skill.asReversed().withIndex()) {
        when (s) {
            1 -> cards.addFirst(i + 1)
            2 -> cards.add(1, i + 1)
            3 -> cards.addLast(i + 1)
            else -> throw Exception("이런 일은 안 일어남.")
        }
    }
    println(cards.joinToString(" "))
}

fun main() {
    readLine()
    sol(readLine()!!.split(" ").map { it.toInt() })
}