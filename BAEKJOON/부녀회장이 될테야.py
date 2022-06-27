# 2775번 - 부녀회장이 될테야

from sys import *
input = stdin.readline

for _ in range(int(input())):
    F, N = int(input()), int(input())
    floor = [ [i for i in range(1,N+1)] for _ in range(F) ]

    for f in range(1,F) :
        for n in range(N) :
            floor[f][n] = sum(floor[f-1][:n+1])
    print(sum(floor[F-1][:N]))



## 다른 사람 풀이
# - 전 층의 해당 호수 + 현재 층의 이전 호수 == 해당 층, 호수에 살아야 할 사람 수 

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])
