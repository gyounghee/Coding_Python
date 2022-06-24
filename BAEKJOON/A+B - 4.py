# 10951번 - A+B - 4
# - 예외 처리 때문에 약간 애먹음.. 

from sys import stdin

input = stdin.readline
while True :
    try :
        a, b = map(int, input().split())
        print(a+b)
    except ValueError :
        break
