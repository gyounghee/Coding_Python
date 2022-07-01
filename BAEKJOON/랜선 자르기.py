# 1654번 - 랜선 자르기

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 100 ms

from sys import *
input = stdin.readline

K, N = map(int, input().split())
cable = [int(input()) for _ in range(K)]

def solution(cable, N) :
    mn,mx = 1, max(cable)
    while mn <= mx :
        p = (mn + mx) // 2
        cut = sum([c//p for c in cable])
        if cut < N :
            mx = p-1
        else :
            mn = p+1
    return mx

print(solution(cable, N))



## 다른 사람 풀이 
# - 메모리 : 30840 KB  /  시간 : 88 ms

from sys import stdin

K, N = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))

h, l = sum(li)//N, 1

while l <= h :
    mid = (h+l)//2
    cnt = sum([x//mid for x in li])
    if cnt < N:
        h = mid - 1
    elif cnt >= N:
        l = mid + 1
        ans = mid
print(ans)
