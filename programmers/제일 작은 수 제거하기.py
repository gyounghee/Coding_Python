# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성하라
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하

def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0 :
        return [-1]
    else :
        return arr


# TEST CASE Ⅰ
arr = [4,3,2,1]
print(solution(arr))

# TEST CASE Ⅱ
arr = [10]
print(solution(arr))
