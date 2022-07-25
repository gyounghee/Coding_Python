# 2644번 - 촌수계산

## 내 풀이 
# - 메모리 : ? KB  /  시간 : ? ms

#from collections import deque
from sys import *
input = stdin.readline

def DFS(n) :
    global ans
    if n2 in p[n] : return True
    if not visited[n]:
        visited[n] = True 
        ans += 1
        for i in p[n]:
            DFS(i)
        

p = [[] for _ in range(int(input())+1)]
n1, n2 = map(int, input().split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    p[x].append(y); p[y].append(x)

visited = [False]* len(p)
ans = -1
print(ans if DFS(n1) else -1)

