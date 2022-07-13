# 7576번 - 토마토

## 내 풀이 
# - 메모리 : 97988 KB  /  시간 : 2008 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(x,y) :
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < r and yy < c and xx >= 0 and yy >= 0 and t[xx][yy] == 0 :
            t[xx][yy] = 1
            tmp.append((xx,yy))

dx, dy = [-1,1,0,0], [0,0,-1,1]
c, r = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(r)]

n = deque([ (i,j) for i in range(r) for j in range(c) if t[i][j] == 1 ])
ans = -1
while n :
    ans += 1
    tmp = deque([])
    for _ in range(len(n)):
        x, y = n.popleft()
        BFS(x,y)
    n = tmp

for i in range(r):
    if t[i].count(0) :
        ans = -1
        break
print(ans)
