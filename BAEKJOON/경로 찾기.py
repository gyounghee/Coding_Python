# 11403번 - 경로 찾기

## 내 풀이 
# - 메모리 : 30840 KB  /  시간 : 432 ms

from sys import *
input = stdin.readline

n = int(input())
g = [ input().split() for _ in range(n) ]
l = [[] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if g[i][j] == '1' : l[i].append(j)

for i in range(n) :
    for j in l[i] :
        for jj in l[j] :
            if jj not in l[i] :
                l[i].append(jj)
                g[i][jj] = '1'

for i in range(n):
    print(' '.join(g[i]))
