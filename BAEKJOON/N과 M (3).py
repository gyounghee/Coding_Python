# 15651번 - N과 M (3)

# 메모리 초과
from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())

perm = list(combinations(list(range(1,N+1)) * M, M)) # 순열 생성
s = list(set([ ''.join(list(map(str, p))) for p in perm ]))

s.sort()
for s in s :
    print(' '.join(s))
