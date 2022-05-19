# 1. Two Sum
# - nums라는 list에서 두 수의 합이 target이 되는 두 수의 index를 출력

# 내 풀이 & 책 풀이 - 1. 부르트 포스로 계산
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        

#### 책 풀이 - 2. in을 이용한 검색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            find = target - n
            
            if find in nums[i+1:]:
                return [i, nums[i+1:].index(find)+(i+1)]

#### 책 풀이 - 3. 첫 번째 수를 뺀 결과 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = collections.defaultdict(int)
        for i,n in enumerate(nums):
            num_dic[n] = i    # 키 : 값 == { 숫자 : 인덱스 }로 저장
        
        # target에서 첫 번째 수를 뺸 결과를 키로 조회
        for i, n in enumerate(nums):
            if target - n in num_dic and i != num_dic[target-n]:
                return [i,num_dic[target-n]]

#### 책 풀이 - 4. 조회 구조 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i, n in enumerate(nums):
            if target - n in num_dic :
                return [ num_dic[target - n], i ]
            num_dic[n] = i

#### 책 풀이 - 5. 투 포인터 이용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == right :
            if nums[left] + nums[right] < target :
                left += 1
            elif nums[left] + nums[right] > target :
                right -= 1
            else :
                return [left, right]
