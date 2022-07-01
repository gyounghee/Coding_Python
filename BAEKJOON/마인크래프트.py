# 18111번 - 마인크래프트

## 내 풀이 (PyPy3)
# - 메모리 : 135540 KB  /  시간 : 564 ms
from sys import *
input = stdin.readline

R, C, B = map(int, input().split())
p = sorted(sum([list(map(int, input().split())) for _ in range(R)], []), reverse=True)
mx = 257 if p[0] > 256 else p[0]+1
time = [float('inf'), 0]

for h in range(0, mx) :
    t, box, stop = 0, B, 1
    for i in range(len(p)) :
        diff = abs(h-p[i])
        if p[i] < h and box < diff :  # 블록이 필요한데 박스가 없다면
            stop = 0
            break
        elif p[i] < h and box >= diff :  # 블록이 필요한데 박스가 있다면
            box -= diff
            t += diff
        elif p[i] > h :   # 블록을 빼야한다면
            box += diff
            t += 2*diff
            
    if t <= time[0] and stop:
        time = [t, h]

print(time[0], time[1])




## 다른 사람 풀이 (python3)
# - 메모리 : 32952 KB  /  시간 : 128 ms

import sys
from math import *
input=sys.stdin.readline
def sol():
    n,m,b=map(int,input().split())
    data=[0]*257
    for _ in range(n):
        for i in map(int,input().split()):
            data[i]+=1
    have=sum(i*data[i] for i in range(257))
    ans=(have*2,0)
    need=0
    t=data[0]
    nm=n*m
    for i in range(1,257):
        need+=t
        have-=nm-t
        t+=data[i]
        if have+b-need<0:
            break
        else:
            ans=min((have*2+need,-i),ans)
    print(ans[0],-ans[1])
sol()
