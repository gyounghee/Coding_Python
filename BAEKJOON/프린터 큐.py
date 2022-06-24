# 1966번 - 프린터 큐

from collections import deque
from sys import *
input = stdin.readline

for tc in range(int(input())) :
    N, M = map(int, input().split())
    n_list = deque([ (n,i) for i, n in enumerate(list(map(int, input().split()))) ])
    f = 0
    
    while True:
        if n_list[0][1] == M and n_list[0][0] == max(n_list)[0]:
            print(f+1)
            break
        elif n_list[0][0] == max(n_list)[0] :
            deque.popleft(n_list)
            f += 1
        else :
            n_list.append((deque.popleft(n_list)))
