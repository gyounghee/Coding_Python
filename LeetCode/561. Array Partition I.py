# 561. Array Partition I
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

# 내 답안 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum = 0
        while nums :
            min_sum += min( nums.pop(), nums.pop() )
        return min_sum


#### 책 풀이 - 1. 오름차순 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n_sum, pair = 0, []
        
        for n in nums :
            pair.append(n)
            if len(pair) == 2:
                n_sum += min(pair)
                pair = []
        return n_sum


#### 책 풀이 - 2. 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n_sum = 0
        nums.sort()
        
        for i, n in enumerate(nums):
            if i % 2 == 0 :
                n_sum += n
        return n_sum


# 2번 풀이에 대한 내 답안
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        nums.sort()
        return sum(nums[::2])


#### 책 풀이 - 3. 파이썬다운 방식
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
