# 11399번 - ATM
# Greedy 알고리즘을 이용한 문제풀이

people = int(input())
spend = list(map(int, input().split()))

spend_sort = sorted(spend)
for i in range(1,len(spend_sort)) :
    spend_sort[i] = spend_sort[i-1] + spend_sort[i]
print(sum(spend_sort))
