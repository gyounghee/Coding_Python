# 5430번 - AC

## 내 풀이 
# - 메모리 : 39172 KB  /  시간 : 272 ms

from collections import deque
from sys import *
input = stdin.readline

for tc in range(int(input())):
    cmd = input().rstrip().replace('RR','')
    int(input())
    n = input().rstrip().replace('[','').replace(']','').replace(',',' ')
    n_lst = deque(list(map(int, n.split())))
    r, e = 0, 0   # r : 뒤집기 기능, e : error 발생 여부 
    for c in cmd :
        if c == 'R' :
            if not r : r = 1  # 뒤집기 기능 비활성화일 경우 :  기능 on
            else : r = 0    # 뒤집기 기능 활성화일 경우 :  기능 off
        elif c == 'D' and n_lst :
            if r : n_lst.pop()  # 뒤집기 기능 활성화인 경우 : 맨 끝 요소 뺌
            else : n_lst.popleft()   # 뒤집기 기능 비활성화인 경우 : 앞에꺼 뺌
        else : e = 1; break
    if e : print('error')
    else :
        n_lst = list(n_lst)
        print(str(n_lst[::-1]).replace(' ','') if r else str(n_lst).replace(' ',''))
    
        
