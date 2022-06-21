# 15650번 - N과 M (2)

from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split())

perm = list(permutations(list(range(1,N+1)), M)) # 순열 생성
s = list(set([ ''.join(list(map(str, sorted(p)))) for p in perm ]))
s.sort()

for c in s :
    print(' '.join(c))
