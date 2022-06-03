# 110474번 - 동전 0
# Greedy 알고리즘을 이용한 문제풀이

coin, goal = map(int, input().split())    # 동전 종류의 수, 동전으로 만들어야 할 돈
coin_v = [int(input()) for _ in range(coin) ]  # 동전의 가치
use = 0   # 사용한 동전 개수

for c in range(coin-1,-1,-1)  :
    use += goal // coin_v[c]
    goal = goal % coin_v[c]

print(use)
