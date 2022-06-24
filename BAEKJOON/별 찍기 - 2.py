# 2439번 - 별 찍기 - 2
# 표준입출력 활용

from sys import *

input = stdin.readline
n = int(input())

for i in range(1,n+1):
    print(('*'*i).rjust(n))
