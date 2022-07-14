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





## 다른 사람 풀이
# - DFS 이용
# - 메모리 : 30840 KB  /  시간 : 84 ms

n = int(input())

adj_list = [[] for i in range(n)]   # 간선을 나타내기 위한 list 생성 
for i in range(n):
    temp = list(map(int, input().split()))
    adj_list[i] = [idx for idx, value in enumerate(temp) if value == 1]
    
def dfs(a, visit):
    for ad in adj_list[a]:
        if visit[ad] == 0:
            visit[ad] = 1
            dfs(ad, visit)

for i in range(n):
    visit = [0]*n
    dfs(i,visit)
    print(*visit)
