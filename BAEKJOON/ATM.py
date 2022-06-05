# 11399번 - ATM
# Greedy 알고리즘을 이용한 문제풀이

people = int(input())  # 줄 서있는 사람 수 
spend = list(map(int, input().split()))  # 각 사람당 소요하는 시간 

spend.sort() # 인출하는데 필요한 시간의 합의 최솟값을 찾기 위해 정렬
for i in range(1,len(spend)) :  
    spend[i] = spend[i-1] + spend[i]  # 해당 위치의 전 값과 본인 값을 더하여 인출하는데 필요한 시간의 합을 구함
print(sum(spend))
