# 2805번 - 나무 자르기

from sys import *
input = stdin.readline

N, M = map(int, input().split()) 
tree = list(map(int, input().split()))

mn, mx = 0, max(tree)-1

while mn <= mx :
    p = (mx+mn)//2
    s = 0
    for t in tree :
        if t>p : s += t-p
        if s > M : break
        
    if s >= M :
        mn = p+1
    else :
        mx = p-1

print(mx)
