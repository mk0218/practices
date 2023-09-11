/* https://school.programmers.co.kr/learn/courses/30/lessons/84512 */

class Solution {
    fun solution(word: String): Int {
        var wd = "A"
        var cnt = 1

        while (wd != word) {
            wd = increment(wd)
            cnt += 1
        }

        return cnt
    }
    
    fun increment(word: String): String = if (word.length < 5) {
        word + 'A'
    } else {    // word.length == 5
        when (word[4]) {
            'A', 'E', 'I', 'O' -> buildString {
                append(word.substring(0..3))
                append(nextChar(word[4]))
            }
            else -> {   // 'U'
                buildString {
                    for (i in 4 downTo 0) {
                        if (word[i] != 'U') {
                            append(word.substring(0..(i-1)))
                            append(nextChar(word[i]))
                            break
                        }
                    }   
                }
            }
        } 
    }
    
    
    fun nextChar(c: Char): Char {
        return when (c) {
            'A' -> 'E'
            'E' -> 'I'
            'I' -> 'O'
            'O' -> 'U'
            else -> throw Exception("다음은 없다..")
        }
    }
}