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
