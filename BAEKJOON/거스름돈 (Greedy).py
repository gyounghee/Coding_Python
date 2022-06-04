# 5585번 - 거스름돈
# Greedy 알고리즘을 이용한 문제풀이 

change = 1000 - int(input())
money = [500,100,50,10,5,1]
ans = 0

for m in money :
    if not change : break
    ans += change // m
    change = change % m

print(ans)
    
