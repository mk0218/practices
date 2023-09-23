# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    boats_waiting, boats_left = [], 0
    
    people.sort(reverse=True)
    
    for w in people:
        if not boats_waiting or boats_waiting[-1] < w:
            boats_waiting.append(limit - w)
        else:
            boats_waiting.pop()
            boats_left += 1
    
    return len(boats_waiting) + boats_left
