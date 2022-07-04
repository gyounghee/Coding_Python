# 2606번 - 바이러스

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

from sys import *
input = stdin.readline

c = int(input())
link = [[] for _ in range(c+1)]
ans = []

for _ in range(int(input())) :
    f,b = map(int, input().split())
    link[f].append(b)
    link[b].append(f)

def linked(l) :
    for p in link[l] :
        if p not in ans and p != 1 :
            ans.append(p)
            linked(p)
    return ans

print(len(linked(1)))




## 다른 사람 풀이
# - 메모리 : 29200 KB  /  시간 : 64 ms

class Remocon:   # 버튼 생성
    def __init__(self):
        self.buttons = list(range(10))
    
    def distroy(self, b):  # 버튼 제거
        self.buttons.remove(b)
    
    def __getitem__(self, n):    # 클래스의 인덱스에 접근할 때 자동으로 호출되는 메서드
        l = len(self.buttons)  
        result, digit = 0, 1    
        while n >= l:  
            result += self.buttons[n%l] * digit  
            n //= l          
            if self.buttons[0]:  
                n -= 1          
            digit *= 10    
        result += self.buttons[n%l] * digit 
        return result
    
    def least_button_push(self, target):
        if not self.buttons:  
            result = float('inf')  
        elif self.buttons == [0,]: 
            result = target + 1 
        elif self[0] > target: 
            result = self[0] - target + 1  
        else: 
            lo, hi = 0, 10
            while self[hi] <= target:  
                hi *= 10
            while hi - lo > 1:      #  이분 탐색
                m = (lo + hi) // 2  
                if self[m] < target:
                    lo = m
                else:
                    hi = m
            lower, higher = self[lo], self[hi]
            result = min(len(str(lower)) + abs(lower - target),
                        len(str(higher)) + abs(higher - target))
        return min(result, abs(target - 100))


remocon = Remocon()  # 리모콘 버튼 생성
target = int(input())   # 목표 채널
if int(input()):    # 고장난 버튼이 있다면
    for button in map(int, input().split()):  # 고장난 버튼 입력
        remocon.distroy(button) # 리모콘에서 고장난 버튼 지워주기
print(remocon.least_button_push(target)) # 목표 채널까지 최소로 눌러야하는 횟수
