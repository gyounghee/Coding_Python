# 1620번 - 나는야 포켓몬 마스터 이다솜 

## 내 풀이
# - 메모리 : 52864 KB  /  시간 : 276 ms

from sys import *
input = stdin.readline

N, M = map(int, input().split())
poketmon_c, poketmon_d = {}, {}
for i in range(1,N+1) :
    p = input().rstrip()
    poketmon_d[int(i)] = p; poketmon_c[p]=i

for _ in range(M):
    n = input().rstrip()
    if n.isdigit() : print(poketmon_d[int(n)])
    else : print(poketmon_c[n])




## 다른 사람 풀이
# - 메모리 : 53464 KB  /  시간 : 188 ms
# - list에 포켓몬 이름을 저장하고, list와 zip()을 이용하여 문제 해결

import sys

def sol():
    input=sys.stdin.readline
    n, m = map(int,input().split())
    dd = [0] + [input().strip() for i in range(n)]  # 포켓몬 이름이 저장된 list
    d=dict(zip(dd,range(n+1)))  # key가 번호, value가 포켓몬 이름인 dictionary
    ans=[dd[int(t)]if (t:=input().strip()).isdigit() else str(d[t]) for i in range(m)]
    print("\n".join(ans))
    
sol()
