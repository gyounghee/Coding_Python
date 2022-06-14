# 11650번 - 좌표 정렬하기

from sys import stdin

numbers = [ list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline())) ]
numbers.sort(key=lambda x : (x[0],x[1]))

for n in numbers :
    print(n[0],n[1]) 
