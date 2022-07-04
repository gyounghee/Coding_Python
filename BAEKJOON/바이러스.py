# 2606번 - 바이러스

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from sys import *
input = stdin.readline

c = int(input())
link = [[] for _ in range(c+1)]
ans = []

for _ in range(int(input())) :
    f,b = map(int, input().split())
    link[f].append(b)
    link[b].append(f)

def linked(l) :
    for p in link[l] :
        if p not in ans and p != 1 :
            ans.append(p)
            linked(p)
    return ans

print(len(linked(1)))
