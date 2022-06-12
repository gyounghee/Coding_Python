# 1259번 - 팰린드롬수

from sys import stdin

while True :
    n = stdin.readline().strip()
    if n == '0' : break
    if n == n[::-1] :
        print('yes')
    else :
        print('no')
