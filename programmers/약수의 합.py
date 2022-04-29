def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0: answer += i
    return answer

# TEST CASE Ⅰ
n = 12
print(solution(n))

# TEST CASE Ⅱ
n = 5
print(solution(n))



# 다른 사람 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상됨
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
