# 9095번 - 1, 2, 3 더하기

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from sys import *
input = stdin.readline

n = [0,1,2,4]+[0] * 7

for i in range(4,11):
    n[i] = n[i-3]+n[i-2]+n[i-1]

for _ in range(int(input())):
    print(n[int(input())])


## 다른 사람 풀이
# - 메모리 : 29284 KB  /  시간 : 52 ms

N = int(input())

arr=[1,2,4]

for i in range(4,11):
    arr.append(sum(arr[-3:]))
    
for _ in range(N):
    T = int(input())
    print(arr[T-1])
