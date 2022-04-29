# array의 각 element 중 divisor로 나누어 떨어지는 값을
# 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성하라

def solution(arr, divisor):
    answer = []
    for n in arr :
        if n % divisor == 0 :
            answer.append(n)
    if len(answer) == 0:
        answer = [-1]
    return sorted(answer)


# TEST CASE Ⅰ
arr, divisor = [5, 9, 7, 10], 5
print(solution(arr, divisor))

# TEST CASE Ⅱ
arr, divisor = [2, 36, 1, 3], 1
print(solution(arr, divisor))

# TEST CASE Ⅲ
arr, divisor = [3,2,6], 10
print(solution(arr, divisor))


# 다른 사람 풀이
def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
