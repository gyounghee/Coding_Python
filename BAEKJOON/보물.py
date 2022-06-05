# 1026번 - 보물
# Greedy 알고리즘을 이용한 문제풀이

## 풀이 1 - B 복사해서 정렬
# - 68ms
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_copy = sorted(B).copy()
A.sort(reverse = True)

AB_sum = 0

for a, b in zip(A,B_copy):
    AB_sum += a * b
    
print(AB_sum)



## 풀이 2 - list의 값 변경 이용
# - 80ms
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB_sum = 0
A.sort()
for a in A :
    AB_sum += a * max(B)
    B[ B.index(max(B)) ] = -1 
    
print(AB_sum)


## 풀이 3 - pop()이용
# - 68ms
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB_sum = 0
A.sort()
for a in A :
    b_max = max(B)
    AB_sum += a * b_max
    B.pop( B.index(b_max) )
    
print(AB_sum)
