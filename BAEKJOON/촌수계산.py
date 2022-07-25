# 2644번 - 촌수계산

## 내 풀이 
# - 메모리 : 30840 KB  /  시간 : 76 ms

from sys import *
input = stdin.readline

def DFS(n) :
    global ans
    if visited[n2] : return True
    if not visited[n] : 
        visited[n] = True 
        ans += 1
        for i in p[n]:
            if DFS(i) : return True
        ans -= 1
        
p = [[] for _ in range(int(input())+1)]
n1, n2 = map(int, input().split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    p[x].append(y); p[y].append(x)

visited = [False]* len(p)
ans = -1
DFS(n1)
print(ans if visited[n2] else -1)
