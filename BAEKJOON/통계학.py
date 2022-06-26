# 2108번 - 통계학

from collections import defaultdict
from sys import *
input = stdin.readline

n = [ int(input()) for _ in range(int(input())) ]
n.sort()

n_dict = defaultdict(int)
for i in n :
    n_dict[i] += 1

mode = [ k for k, v in n_dict.items() if v == max(n_dict.values()) ]

print( int(round(sum(n)/len(n), 0)) )
print( n[len(n)//2] )
print( sorted(mode)[1] if len(mode) > 1 else mode[0])
print( max(n)-min(n))
