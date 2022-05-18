# 42. Trapping Rain Water
# - 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산

#### 책 풀이 - 1. 투 포인터를 최대로 이동 
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : 
            return 0
        
        water = 0
        left, right = 0, len(height) - 1 
        left_max, right_max = height[left], height[right]
        
        while left < right :
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # 더 높은 곳을 향해서 포인터 이동
            if left_max <= right_max :
                water += left_max - height[left]
                left += 1
            else : 
                water += right_max - height[right]
                right -= 1
        return water
