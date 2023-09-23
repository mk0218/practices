/* https://school.programmers.co.kr/learn/courses/30/lessons/42861 */

import java.util.PriorityQueue

class Solution {
    fun solution(n: Int, costs: Array<IntArray>): Int {
        val costsFrom = costsBySrc(n, costs)
        var nextEdges = PriorityQueue<Cost>(costs.size)
        var connected = hashSetOf<Int>()
        var cost = 0
        
        connected.add(0)
        nextEdges.addAll(costsFrom[0])
        
        while (connected.size < n) {
            val edge = nextEdges.remove()
            
            if (connected.contains(edge.dst)) {
                continue
            }
            
            connected.add(edge.dst)
            nextEdges.addAll(costsFrom[edge.dst])

            cost += edge.cost
        }

        return cost
    }
    
    fun costsBySrc(n: Int, costs: Array<IntArray>): Array<ArrayList<Cost>> {
        var result = Array<ArrayList<Cost>>(n) { arrayListOf() }
        
        for ((src, dst, cost) in costs) {
            result[src].add(Cost(dst, cost))
            result[dst].add(Cost(src, cost))
        }
        
        return result
    }
}

class Cost(dst: Int, cost: Int): Comparable<Cost> {
    val dst = dst
    val cost = cost
    
    override fun compareTo(other: Cost): Int {
        return cost.compareTo(other.cost)
    }
}