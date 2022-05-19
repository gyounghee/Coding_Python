# 238. Product of Array Except Self
# - 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

# ** 제한사항 **
# - 나눗셈을 하지 않고 O(N)에 풀이하라

# 내 답안 - 시간 초과 이슈 발생
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = collections.deque(nums)
        ans = []
        
        for _ in range(len(nums)) : 
            tmp = nums.popleft()
            if [0] in nums :
                ans.append(0)
            else : 
                ans.append( functools.reduce(lambda x, y : x * y, nums) )
            nums.append(tmp)
            
        return ans


#### 책 풀이 - 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
# - 자기자신을 제외한 왼쪽의 곱셈결과와 오른쪽의 곱셈결과를 곱한다

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
