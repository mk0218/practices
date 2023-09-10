/* https://www.acmicpc.net/problem/22859 */

enum class HTML {
    MAIN,
    DIV,
    P,
    ELSE,
    NONE,
}

enum class BS {
    IDLE,
    WORD,
    SPACE,
}

fun parseHtml(html: String) {
    var line = StringBuilder()
    var block = arrayListOf<HTML>()
    var buffer = StringBuilder()
    var bufState = BS.IDLE
    var parsingTag = false
    var tagBuffer = StringBuilder()

    for (c in html) {
        when (c) {
            '<' -> {    // Tag parsing start
                parsingTag = true
            }
            '>' -> {    // Tag parsing end. Identify tag.
                val (tag, title) = parseTag(tagBuffer)
                if (tag == block.lastOrNull() ?: HTML.NONE) {
                    // Block ended. Pop from the 'block' stack.
                    block.removeLastOrNull()

                    if (tag == HTML.P) {
                        // If block was '<p>', add buffer content to line,
                        // then print content and clear line buffer.
                        if (bufState == BS.WORD) {
                            line.append(buffer)
                            buffer.clear()
                        }
                        println(line.trim().toString())
                        bufState = BS.IDLE
                        line.clear()
                    }
                } else if (tag != HTML.ELSE) {
                    // Encountered new block. Push to the 'block' stack.
                    block.add(tag)

                    if (tag == HTML.DIV) {
                        // If the tag is div-open tag, print the title line.
                        println("title : $title")
                    }

                }
                parsingTag = false
                tagBuffer.clear()
            }
            else -> {
                if (parsingTag) {   // Parsing tag -> append to tag buffer.
                    tagBuffer.append(c)
                } else if (!parsingTag && block.lastOrNull() ?: HTML.NONE == HTML.P) {
                    // Parsing Paragraph content. append to buffer.
                    when (c) {
                        ' ' -> {
                            if (bufState == BS.WORD) {
                                // bufState: WORD -> SPACE, buf content to line.
                                line.append(buffer)
                                buffer.clear()
                                bufState = BS.SPACE
                            }
                        }
                        else -> {
                            if (bufState != BS.WORD) {
                                // bufState: SPACE, IDLE -> WORD, buf content to line.
                                if (bufState == BS.SPACE) {
                                    line.append(' ')
                                }
                                buffer.clear()
                            }
                            bufState = BS.WORD
                        }
                    }
                    buffer.append(c)
                }
            }
        }
    }
    if (bufState == BS.WORD) {
        line.append(buffer)
    }

    if (line.length > 0) {
        println(line.trim().toString())
    }
}

fun parseTag(tagContent: StringBuilder): Pair<HTML, String> {
    var buffer = StringBuilder()
    var tag: HTML? = null
    var title = ""
    var parsingTitle = false

    fun getTag(t: String) = when (buffer.trim().toString()) {
        "main", "/main" -> HTML.MAIN
        "div", "/div" -> HTML.DIV
        "p", "/p" -> HTML.P
        else -> HTML.ELSE
    }

    for (c in tagContent) {
        when (c) {
            '"' -> {
                if (tag ?: HTML.ELSE == HTML.DIV) {
                    when (parsingTitle) {
                        true -> {
                            title = buffer.toString()
                            buffer.clear()
                            break
                        }
                        false -> {
                            buffer.clear()
                            parsingTitle = true
                        }
                    }
                }
            }
            ' ' -> {
                if (buffer.length > 0 && tag == null) {
                    // Get html tag type.
                    tag = getTag(buffer.trim().toString())
                    buffer.clear()
                } else if (parsingTitle) {
                    buffer.append(c)
                }
            }
            else -> {
                buffer.append(c)
            }
        }
    }

    if (buffer.length > 0 && tag == null) {
        tag = getTag(buffer.trim().toString())
    }

    return Pair(tag ?: HTML.ELSE, title)
}

fun main() {
    parseHtml(readLine()!!)
}