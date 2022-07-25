# 2644번 - 촌수계산

## 내 풀이 
# - 메모리 : 30840 KB  /  시간 : 72 ms

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
        
p = [[] for _ in range(int(input())+1)]  # 연결 관계 입력을 위한 list 생성
n1, n2 = map(int, input().split())       # 촌수를 계산해야하는 두 사람의 번호
for _ in range(int(input())):            # p(연결 관계 list) 초기화 
    x, y = map(int, input().split())
    p[x].append(y); p[y].append(x)

visited = [False]* len(p)  # 방문 여부 check 
ans = -1   
DFS(n1)  
print(ans)
