# 콜라츠 추측

# 풀이 1
def solution(num) :
    answer = 0
    while num > 1 :
        if answer == 500 : return -1
        num = num//2 if num  % 2 == 0 else num*3+1
        answer += 1
    return answer



# 풀이 2 :
def solution(num) :
    for i in range(500) :
        if num == 1 : 
            return i
        else :
            num = num//2 if num  % 2 == 0 else num*3+1
    return -1
