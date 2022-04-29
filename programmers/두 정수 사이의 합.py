def solution(a, b):
    answer = 0
    big, small = max(a,b), min(a,b)

    for i in range(small, big+1):
        answer+= i
    return answer

# TEST CASE Ⅰ   →   12
a, b = 3, 5
print(solution(a, b))

# TEST CASE Ⅱ   →   3
a, b = 3, 3
print(solution(a, b))

# TEST CASE Ⅲ   →   12
a, b = 5, 3
print(solution(a, b))
