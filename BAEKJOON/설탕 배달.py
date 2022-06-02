# 2839번 - 설탕 배달

suger = int(input())

big, small = 5, 3
use = []

for n in range(suger//big + 1):
    tmp_suger = suger - big * n
    if tmp_suger % small == 0 :
        use.append( n + tmp_suger // small)

if len(use) :
    print(min(use))
else :
    print(-1)
