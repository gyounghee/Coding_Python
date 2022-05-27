# 최솟값 만들기

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    while len(A) :
        answer += A.pop() * B.pop()
    return answer


# TEST CASE Ⅰ
A, B = [1, 4, 2], [5, 4, 4]
print(solution(A, B))      # 29

# TEST CASE Ⅱ
A, B = [1,2], [3,4]
print(solution(A, B))      # 20



# 다른 사람 풀이
# 나처럼 꺼내서 푸는 것이 아닌 zip() 함수를 이용하여 바로 계산
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
