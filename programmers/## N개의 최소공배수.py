####### 하....통과 못함 다시 풀어보
# GCD = 최대공약수
# LCM = 최소공배수
# ( a, b )의 최소공배수 →  a * b = GCD * LCM

# [ 유클리드 호제법 ]
# 두 수 a, b (a > b) 가 있을 때
# a % b == 0 이면, GCD(최대공약수)는 b
# a % b != 0 이면 (c = a % b라고 할 때)
# b % c 를 구해서 0이 나올 때 까지 반복

from functools import reduce

def solution(arr):
    arr.sort()
    a, b, GCD = 0, 0, []
    for n in arr[1:] :
        if len(GCD) == 0 :
            a, b = arr[0], n
        else :
            a = n
            b = min(GCD)

        while True:
            if a % b == 0 and a >= b:
                GCD.append(b)
                break
            else :
                a, b = b, a % b

    total = reduce(lambda x, y : x*y, arr)
    GCD = reduce(lambda x, y : x*y, GCD)

    return total // GCD

arr = [2,6,8,14]
print(solution(arr))    # 168

arr = [1,2,3]
print(solution(arr))    # 6

arr = [3, 4, 9, 16]
print(solution(arr))    # 144



[5,10,15,20,25] 300
[1,10,100,1000,5000,3,9999] 49995000
[1,2,3,4,5,6,7,8,9,10] 2520
