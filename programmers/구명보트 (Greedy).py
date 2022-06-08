# 구명보트 (Greedy)

# 12m
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


### 다른 사람 풀이
# - 투 포인터를 이용한 풀이
# - 짝 지었을때만 2명씩 나가기 때문에 전체 인원에서 짝 지은 수만 빼주면 보트의 수가 나오는 것을 이용
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
