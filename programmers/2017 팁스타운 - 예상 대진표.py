# 2017 팁스타운 - 예상 대진표
def solution(n,a,b):
    answer = 1
    a,b = min(a,b), max(a,b)
    
    while abs(a-b) != 1 or b %2 == 1:
        if a != 1 :
            a = a//2 if a % 2 == 0 else (a//2)+1 
        b = b//2 if b % 2 == 0 else (b//2)+1     
        answer += 1
    return answer
