def solution(x):
    x_sum = sum(list(map(int, list(str(x)))))
    return True if x % x_sum == 0 else False

# TEST CASE 
arr = 10
print(solution(arr))   # true
arr = 12
print(solution(arr))   # true
arr = 11
print(solution(arr))   # false
arr = 13
print(solution(arr))   # false


## 다른 사람 풀이
# str과 for문 & 비교 연산자 사용 
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0
