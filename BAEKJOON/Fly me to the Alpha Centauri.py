# 1011번 - Fly me to the Alpha Centauri

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 1520 ms
from sys import *
input = stdin.readline

for _ in range(int(input())) :
    x, y = map(int, input().split())
    s = 1
    ans = 0
    while (y-x) > 0 :
        if (y-x)-s <= 0 :
            ans += 1
            break
        if (y-x)-s*2 >= 0 :
            x, y = x+s, y-s
            s += 1
            ans += 2
        elif (y-x)-s*2 < 0 :
            ans += 2
            break
    print(ans)


## 다른 사람 풀이

# - 메모리 : 30840 KB  /  시간 : 64 ms
import sys
input = sys.stdin.readline

for _ in range(int(input())):
	x,y=map(int, input().split())
	sq=int((y-x-1)**0.5)
	
	if y-x > sq*sq + sq : print(2*sq+1)
	else : print(2*sq)
