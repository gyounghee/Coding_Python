# 행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :   # arr1의 행
        tmp = []
        for j in range(len(arr2[0])) :   # arr2의 열
            num = 0
            for k in range(len(arr1[0])) :   # arr1의 열
                num += arr1[i][k] * arr2[k][j]
            tmp.append(num)
        answer.append(tmp)
    return answer


# 다른 사람 풀이
def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
