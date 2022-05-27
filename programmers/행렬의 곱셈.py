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
def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(arr1_row,arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]
    # arr2의 열을 unpacking하여 풀어서 zip()해준 후 이를 이용하여 행렬곱 수행

