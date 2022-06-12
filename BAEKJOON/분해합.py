# 1092번 - 분해

# 시간 : 676ms
from sys import stdin

n = int(stdin.readline())
find = 0

for i in range(n//2, n):
     if i + sum(map(int,str(n))) == n :
         find = i
         break
print(find)



## 다른 사람 풀이
# 시간 : 68ms 

N=int(input())
r=0

for i in range(max(0, N-100), N):
    if sum(map(int,list(str(i))))+i==N:
        r=i
        break
print(r)
