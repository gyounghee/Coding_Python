# 15. 3Sum

# 내 답안
# - 제한시간 초과 이슈 발생
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        comb = [sorted(c) for c in list(itertools.combinations(nums, 3)) if sum(c) == 0]
        ans = []
        for i in range(len(comb)) :
            if comb[i] not in comb[i+1 : ]:
                ans.append(comb[i])
        return ans



#### 책 풀이 - 1. 부르트 포스로 계산
## - 시간 복잡도가 O(N³)으로 시간초과 이슈 발생 ,
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        # 부르트 포스 n³ 반복
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0 :
                        ans.append([nums[i],nums[j],nums[k]])
        return ans


#### 책 풀이 - 2. 투 포인터로 합계    ( 공부 후 재도전 )
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1] :
                continue
            left, right = i+1, len(nums)-1
            
            while left < right : 
                total = nums[i] + nums[left] + nums[right]

                if total < 0 :
                    left += 1
                elif total > 0 :
                    right -= 1
                else : 
                    ans.append( [nums[i], nums[left], nums[right]] )
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
