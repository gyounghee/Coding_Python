# 4153번 - 직각삼각형

from sys import stdin

while True :
    num = list(map(int, stdin.readline().split()))
    if sum(num) == 0 : break
    else :
        num.sort()
        if num[0]**2 + num[1]**2 == num[2]**2 :
            print('right')
        else :
            print('wrong')
