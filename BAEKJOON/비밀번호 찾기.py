# 17219번 - 비밀번호 찾기

## 내 풀이
# - 메모리 : 49788 KB  /  시간 : 256 ms

from sys import *
input = stdin.readline

N, M = map(int, input().split())

site_pw = {}
for _ in range(N) :
    k, v = input().split()
    site_pw[k] = v

for _ in range(M) :
    print(site_pw[input().rstrip()])
