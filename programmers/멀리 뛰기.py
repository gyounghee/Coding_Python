# 멀리 뛰기
# - 피보나치 수열 이용하여 풀이

## 풀이 Ⅰ
# - list 이용
def solution(n):
    answer = [0,1,2]
    if n < 3 :
            return answer[n]
    else :
        for i in range(3,n+1) :
            answer.append(answer[i-1] + answer[i-2])
        return answer[n] % 1234567


## 풀이 Ⅱ
# -투 포인터 이용
# - 리스트 이용할 때 보다 시간적으로 더 빠름
def solution(n):
    one, two = 1,2
    if n == 1 : 
        return one
    else :
        for i in range(n-2) :
            one, two = two, one+two
        return two % 1234567 
