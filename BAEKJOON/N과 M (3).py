# 15651번 - N과 M (3)

# 풀이 1
from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

rs = []
chk = [False] * (N+1)

def BT(n):
    if n == M :
        print(' '.join(map(str, rs)))
        return
    for i in range(1,N+1):
        if not chk[i] :
            chk[i] == True
            rs.append(i)
            BT(n+1)
            chk[i] == False
            rs.pop()

BT(0)


# 메모리 초과
from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())

perm = list(combinations(list(range(1,N+1)) * M, M)) # 순열 생성
s = list(set([ ''.join(list(map(str, p))) for p in perm ]))

s.sort()
for s in s :
    print(' '.join(s))


