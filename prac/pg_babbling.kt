/* https://school.programmers.co.kr/learn/courses/30/lessons/120956 */

class Solution {

    val dictionary = arrayOf("aya", "ye", "woo", "ma")

    fun solution(babbling: Array<String>): Int {
        var answer: Int = 0
        for (word in babbling) {
            if (canSpeak(word)) answer += 1
        }
        return answer
    }

    fun canSpeak(word: String): Boolean {
        val initials = Array(4) { i -> dictionary[i][0] }
        var wordIndex = -1 // -1: Initialized, 0..3: Dictionary Undex, Else: Error
        var charIndex = 0 // Character index in a word in dictionary

        for (c in word) {
            if (wordIndex == -1) {
                if (c in initials) wordIndex = initials.indexOf(c) else return false
            } else if (c != dictionary[wordIndex][charIndex]) { // Wrong
                return false
            } else if (charIndex == dictionary[wordIndex].length - 1) { // Last character
                wordIndex = -1
                charIndex = 0
                continue
            }
            charIndex += 1
        }

        return if (wordIndex == -1) true else false
    }
}
