# 17219번 - 비밀번호 찾기

## 내 풀이
# - 메모리 : 49788 KB  /  시간 : 256 ms

from sys import *
input = stdin.readline

N, M = map(int, input().split())
ans = []

name = { input().rstrip():0 for _ in range(N) }  
for _ in range(M) :
    try : name[input().rstrip()] +=1 
    except : pass

for k, v in name.items() :
    if v == 1 : ans.append(k)

print(len(ans))
print('\n'.join(sorted(ans)))
