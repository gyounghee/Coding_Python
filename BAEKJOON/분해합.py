from sys import stdin

n = int(stdin.readline())
find = 0

for i in range(n//2, n):
     tmp = list(map(int, list(str(i))))
     if i + sum(tmp) == n :
         find = i
         break

print(find)
