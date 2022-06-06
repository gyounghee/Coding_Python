# 1546번 - 평균

from functools import reduce

n = int(input())
score = list(map(int, input().split()))

max_score = max(score)

score = [ round(i/max_score*100, 2) for i in score ]
total = reduce(lambda x,y : x+y, score)
print( round(total/n, 2) )


## 다른 풀이 
n = int(input())
s = [int(x) for x in input().split()]

ss = sum(s)
print(ss/max(s)*100/n)

