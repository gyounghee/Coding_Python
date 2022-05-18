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


#### 책 풀이 - 2. 스택 쌓기
class Solution:
    def trap(self, height: List[int]) -> int:
        stack, volume = [], 0
        
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]] :
                top = stack.pop()
                
                if not len(stack) :
                    break
                    
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters  = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
            
            stack.append(i)
        return volume
            
