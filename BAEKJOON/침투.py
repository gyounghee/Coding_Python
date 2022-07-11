# 13565번 - 침투

## 풀이 1
# - 메모리 : 36616 KB  /  시간 : 912 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(x,y) :
    q = deque([[x,y]])
    while q :
        x,y = q.popleft()
        if x == r-1 : return 1
        if p[x][y] == 1 : continue
        p[x][y] = 1
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if xx >= r or xx < 0 or yy >= c or yy < 0 or p[xx][yy] == 1: continue
            q.append([xx,yy])
    return 0

dx, dy = [-1,1,0,0], [0,0,-1,1]
r, c = map(int, input().split())
p = [list(map(int, list(input().rstrip()))) for _ in range(r)]
res = 0

for i in range(c) :
    if p[0][i] == 0 :
        if BFS(0,i) == 1 :
            res = 1 ; break

print('YES' if res else 'NO')



## 풀이 2
# - DFS 이용
# - 메모리 : 99084 KB  /  시간 : 296 ms

from sys import *
setrecursionlimit(10**6)
input = stdin.readline

def DFS(x,y) :
    global res
    p[x][y] = "2"
    if x == r-1 : res = 1 
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if not res and xx < r and xx >= 0 and yy < c and yy >= 0 and p[xx][yy] == "0" : 
            DFS(xx, yy)

dx, dy = [-1,1,0,0], [0,0,-1,1]
r, c = map(int, input().split())
p = [list(input().rstrip()) for _ in range(r)]
res = 0
for i in range(c) :
    if p[0][i] == "0" :
        DFS(0,i)
    if res : break
    
print('YES' if "2" in p[-1] else 'NO')




## 다른 사람 풀이 ( DFS 풀이 )
# - 메모리 : 39552 KB  /  시간 : 128 ms

import sys
sys.setrecursionlimit(10**6)
M, N = map(int, sys.stdin.readline().strip().split())

nodeMap = []
for _ in range(M):
    nodeMap.append(sys.stdin.readline().strip())

nodeCk = [[False for _ in range(N)] for _ in range(M)]

nextYX = [(1, 0), (0, 1), (0, -1), (-1, 0)]

res = 'NO'
def dfs(y, x):
    global res
    if y == M - 1:
        res = 'YES'

    nodeCk[y][x] = True
    for Y, X in nextYX:
        nextY = y + Y
        nextX = x + X
        if res != 'YES' and -1 < nextY < M and -1 < nextX < N and nodeMap[nextY][nextX] == '0' and nodeCk[nextY][nextX] == False:
            dfs(nextY, nextX)

for i in range(N):
    if nodeMap[0][i] == '0':
        dfs(0, i)
    
    if res == 'YES':
        break

print(res)
