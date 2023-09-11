/* https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/ */

import kotlin.math.pow

class Solution {
    fun countOrders(n: Int): Int {
        var mem = mutableMapOf<Pair<Int, Int>, ULong>(    // states that pickup a, b, c and delivery a, b, c are all visited.
            Pair(0, 0) to 1.toULong(),
            Pair(1, 0) to 1.toULong(),
            Pair(1, 1) to 1.toULong(),
        )

        for (k in 2..n) {
            mem[Pair(k, 0)] = mod(mem[Pair(k-1, 0)]!! * k.toULong())
            for (i in 1..(k-1)) {
                val state = Pair(k, i)
                val cnt = mod(mem[Pair(k, i-1)]!! * i.toULong()) + mod(mem[Pair(k-1, i)]!! * (k-i).toULong())
                mem[state] = mem[state] ?: 0.toULong() + cnt
            }
            mem[Pair(k, k)] = mod(mem[Pair(k, k-1)]!! * k.toULong())
        }

        return mem[Pair(n, n)]!!.toInt()
    }

    fun mod(n: ULong): ULong {
        return n % (10.toDouble().pow(9).toULong() + 7.toULong())
    }
}