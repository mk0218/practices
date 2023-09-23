/* https://school.programmers.co.kr/learn/courses/30/lessons/42883 */

class Solution {
    fun solution(number: String, k: Int): String {
        var result = ArrayList<Char>(number.length - k)
        
        for (i in 0 .. number.length - 1) { // i <= k + result.size
            while (!result.isEmpty() && result.last() < number[i] && i < k + result.size) {
                result.removeLast()
            }
            if (result.size < number.length - k) {
                result.add(number[i])
            }
        }
        
        
        return result.joinToString("")
    }
}