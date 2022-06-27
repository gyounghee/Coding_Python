# 1744번 - 수 묶기

from sys import *
input = stdin.readline

n = [ int(input()) for _ in range(int(input())) ]
res = 0

n.sort() if max(n) > 0 else n.sort(reverse=True)
while len(n) > 1 :
    a, b = n.pop(), n.pop()
    if a == 1 and b == 1 : res += 2
    elif a == -1 and b == -1 : res += 1
    elif a > 1 and b > 1 or a < 0 and b < 0 or a < 0 and b == 0:
        res += a*b
    elif a > 0 and b <= 1 :
        res += a
        n.append(b)
        n.sort(reverse=True)
        
print( res+n[0] if n else res )
