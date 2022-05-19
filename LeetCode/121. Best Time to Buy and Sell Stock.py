# 121. Best Time to Buy and Sell Stock
# - 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

# 내 답안 - 시간초과 이슈 발생
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] == max(prices) : 
                continue
            for j in range(i+1,len(prices)):
                if -(prices[i] - prices[j]) > profit :
                    profit = -(prices[i] - prices[j])
        return profit


## 책 풀이 - 1. 저점과 현재 값과의 차이 계산  ( 스스로 한번 더 풀어보기ㅜ )
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = max(prices)
        
        # 최솟값과 최댓값을 계속 갱신
        for p in prices:
            min_p = min(min_p, p)
            profit = max(profit, p - min_p)
        
        return profit
