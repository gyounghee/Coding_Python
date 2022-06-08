# 구명보트 (Greedy)

from collections import deque

def solution(people, limit):
    answer = 0
    p = deque(sorted(people))
    
    while len(p) > 1 :
        if p[0] + p[-1] <= limit :
            p.popleft(); p.pop()
        else :
            p.pop()
        answer += 1
        
    return answer if not p else answer + 1


# 12m
