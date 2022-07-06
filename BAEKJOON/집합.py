# 11723번 - 집합

## 내풀이
# - 메모리 : 30840 KB  /  시간 : 3136 ms

from sys import *
input = stdin.readline

S = []

for _ in range(int(input())) :
    cmd= input().split()

    if cmd[0] == 'add' and cmd[1] not in S :
        S.append(cmd[1])
    elif cmd[0] == 'remove' and cmd[1] in S :
        S.remove(cmd[1])
    elif cmd[0] == 'check' :
        print(1 if cmd[1] in S else 0)
    elif cmd[0] == 'toggle' :
        if cmd[1] in S  : S.remove(cmd[1])
        else : S.append(cmd[1])
    elif cmd[0] == 'all' :
        S = ['1','2','3','4','5','6','7','8','9','10',
             '11','12','13','14','15','16','17','18','19','20']
    elif cmd[0] == 'empty' :
        S = []


## 다른 사람 풀이
# - Bitmask 이용
# - 메모리 : 30840 KB  /  시간 : 2872 ms

s = 0
l = open(0)
# 파일에서 다음번 행 반환
# 즉, 수행해야하는 연산의 수를 입력한 후의 줄로 커서를 옮김
next(l)  

# for문을 통해 하나씩 살펴봄
# - 여기서 cmd[-2:]를 하는 이유는 최대로 올 수 있는 수가 2자리이기 때문
for cmd in l:
    if cmd[0] == 'e':     # empty
        s = 0
    elif cmd[0] == 'c':   # check
        print((s >> int(cmd[-2:])) & 1)
    elif cmd[0] == 't':   # toggle
        s = s ^ (1<<int(cmd[-2:]))
    elif cmd[0] == 'r':   # remove
        s = s & ~(1<<int(cmd[-2:]))
    elif cmd[1] == 'd':   # add
        s = s | (1<<int(cmd[-2:]))
    else:                 # all
        s = ~0
