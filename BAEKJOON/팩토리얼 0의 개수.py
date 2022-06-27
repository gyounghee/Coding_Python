# 1676번 - 팩토리얼 0의 개수

from functools import reduce

n = int(input())
if n == 0 : print(0)
else :
    n = str(reduce(lambda x,y : x*y, list(range(1,n+1))))
    for i in range(len(n)):
        if n[::-1][i] != '0' :
            print(i)
            break
