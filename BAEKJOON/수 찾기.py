# 1920번 - 수 찾기

from sys import stdin

N, A = stdin.readline(), set(map(int, stdin.readline().split()))
M, num = stdin.readline(), list(map(int, stdin.readline().split()))

for i in num :
    if i in A : print(1)
    else : print(0)
