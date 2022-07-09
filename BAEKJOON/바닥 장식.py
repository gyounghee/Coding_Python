# 1388번 - 바닥 장식

## 풀이 1
# - DFS 이용
# - 메모리 : 30840 KB  /  시간 : 76 ms

from sys import *
input = stdin.readline

def DFS(i,j) :
    if stack[-1] == '-' and j < c and h[i][j] == '-'  :
        h[i][j]= 'x'
        DFS(i,j+1)
    elif stack[-1] == '|' and i < r and h[i][j] == '|' :
        h[i][j]= 'x'
        DFS(i+1,j)
    else : return 1
        

r, c = map(int, input().split())
h = [list(input().rstrip()) for _ in range(r)]
ans = 0

for i in range(r) :
    for j in range(c) :
        if h[i][j] != 'x' :
            stack = [h[i][j]]
            DFS(i,j)
            ans += 1

print(ans)




# 1388번 - 바닥 장식

## 풀이 2
# - BFS 이용
# - 메모리 : 32452 KB  /  시간 : 92 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(i,j,s) :
    q = deque([[i,j]])
    while q :
        i, j = q.popleft()
        if i >= r or j >= c : return 1 
        if s == '-' and h[i][j] == '-':
            h[i][j]= 'x'
            q.append([i,j+1])
        elif s == '|' and h[i][j] == '|':
            h[i][j]= 'x'
            q.append([i+1,j])
        else : return 1
        
r, c = map(int, input().split())
h = [list(input().rstrip()) for _ in range(r)]
ans = 0

for i in range(r) :
    for j in range(c) :
        if h[i][j] != 'x' :
            BFS(i,j, h[i][j])
            ans += 1

print(ans)
