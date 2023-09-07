/* https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=kotlin */

class Ticket(index: Int, from: String, dst: String) {
    val index = index
    val from = from
    val dst = dst
}

class Solution() {
    fun solution(tickets_: Array<Array<String>>): Array<String> {
        val tickets = tickets_.mapIndexed { idx, (from, dst) -> Ticket(idx, from, dst) }
        var visited = Array<Boolean>(tickets.size) { false }

        fun getNextTickets(current: String): List<Ticket> {
            return tickets.filter { it.from == current && !visited[it.index] }
                          .sortedBy { ticket -> ticket.dst }
        }

        fun find_route(route: Array<String>): Array<String>? {
            if (route.size == tickets.size + 1) {
                return route
            } else {
                val current = route[route.size - 1]
                val nextTickets = getNextTickets(current)

                if (nextTickets.isEmpty()) {
                    return null
                }
                
                var result: Array<String>? = null

                for (ticket in nextTickets) {
                    visited[ticket.index] = true
                    result = find_route(route + ticket.dst)
                    
                    if (result != null) {
                        break
                    } else {
                        visited[ticket.index] = false
                    }
                }
                return result
            }
        }

        return find_route(arrayOf("ICN"))!!
    }
}

fun main() {
    val tcs = arrayOf(
        arrayOf(
            arrayOf("ICN", "JFK"),
            arrayOf("HND", "IAD"),
            arrayOf("JFK", "HND")
        ),
        arrayOf(
            arrayOf("ICN", "SFO"),
            arrayOf("ICN", "ATL"),
            arrayOf("SFO", "ATL"),
            arrayOf("ATL", "ICN"),
            arrayOf("ATL","SFO")
        )
    )
    for (tc in tcs) {
        println(tc.map { it.joinToString(" ") }.joinToString("\n"))
        println(Solution().solution(tc).joinToString(" "))
    }
}