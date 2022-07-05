# 11659번 - 구간 합 구하기 4 

## 내 풀이
# - 메모리 : 40596 KB  /  시간 : 296 ms

from itertools import accumulate
from sys import *
input = stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
n_sum = list(accumulate(num))

for _ in range(M):
    f, b = map(int, input().split())
    if f == b : print(num[f-1])
    elif f == 1 and b > 1 :
        print( n_sum[b-1] )
    else :
        print( n_sum[b-1] - n_sum[f-2] )



## 다른 사람 풀이
# - 메모리 : 40596 KB  /  시간 : 244 ms     

from itertools import accumulate
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [0] + list(map(int, input().split()))  
p_sum = list(accumulate(ls))
for _ in range(m):
    i, j = map(int, input().split())
    print(p_sum[j] - p_sum[i - 1])
