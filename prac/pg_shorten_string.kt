/* https://school.programmers.co.kr/learn/courses/30/lessons/60057 */

import kotlin.math.min

class Solution {
    fun solution(s: String): Int {
        var length = mutableListOf<Int>()

        fun compress(substr: String, count: Int): String {
            return when (count) {
                0 -> ""
                1 -> substr
                else -> count.toString() + substr
            }
        }

        for (unit in 1 .. (s.length / 2)) {
            var substr = s.substring(0 .. (unit - 1))
            var count = 0
            var compressed = StringBuilder()
            var str = s

            while (true) {
                if (str.length < unit) {
                    compressed.append(compress(substr, count) + str)
                    break
                } else {
                    val prefix = str.substring(0 .. (unit - 1))
                    if (prefix == substr) {
                        count += 1
                    } else {
                        compressed.append(compress(substr, count))
                        substr = prefix
                        count = 1
                    }
                }
                str = str.substring(unit .. (str.length - 1))
            }
            println(compressed)
            length.add(compressed.length)
        }

        return length.fold(s.length) { acc, v -> min(acc, v) }
    }
}

fun main() {
    println(Solution().solution("a"))
}