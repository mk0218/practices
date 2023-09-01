/* https://www.acmicpc.net/problem/1966 */

class Document(id: Int, priority: Int) {
    val id = id
    val priority = priority

    override fun toString(): String {
        return "Document(id: ${id}, priority: ${priority})"
    }
}

class PrinterQueue(size: Int) {
    val queue = ArrayDeque<Document>(size)
    var priority = IntArray(10)
    var count = 0

    fun push(doc: Document) {
        queue.add(doc)
        priority[doc.priority] += 1
    }

    fun checkPriority(p: Int): Boolean {
        for (i in ((p + 1)..9).reversed()) {
            if (priority[i] != 0) {
                return false
            }
        }
        return true
    }

    fun print(): Int {
        while (true) {
            val doc = queue.removeFirst()
            if (checkPriority(doc.priority)) {
                count += 1
                priority[doc.priority] -= 1
                return doc.id
            }
            queue.add(doc)
        }
    }

    fun printUntil(doc: Int): Int {
        while (print() != doc) {}
        return count
    }
}

fun main() {
    for (i in 1..(readLine()!!.toInt())) {
        val (n, m) = readLine()!!.split(" ").map { it.toInt() }
        val pq = PrinterQueue(n)
        readLine()!!.split(" ").mapIndexed { idx, prioirty ->
            pq.push(Document(idx, prioirty.toInt()))
        }
        println(pq.printUntil(m))
    }
}
