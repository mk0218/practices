/* https://school.programmers.co.kr/learn/courses/30/lessons/42842 */

class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var (w, h) = Pair(brown / 2 - 3, 1) // Width, height of >> Yellow << part!!
        
        while (w >= h) {
            if (w * h == yellow) {
                break
            } else {
                w -= 1
                h += 1
            }
        }

        return intArrayOf(w + 2, h + 2)
    }
}

fun main() {
    val testcases = listOf(Pair(10, 2), Pair(8, 1), Pair(24, 24))
    for ((brown, yellow) in testcases) {
        println(Solution().solution(brown, yellow).joinToString(" "))
    }
}