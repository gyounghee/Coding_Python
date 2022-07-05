# 1107번 - 리모컨

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 6316 ms

from sys import *
input = stdin.readline

def ch_minus(N, ch, btn) :
    for n in range(N,-1,-1) :
        if not (set(map(int, str(n))) & set(btn)) :
            return n
    return float('inf')

def ch_plus(N, ch, btn, mn) :
    for n in range(N,8000000) :
        if n-N > mn*100 : return float('inf')
        if not (set(map(int, str(n))) & set(btn)) :
            return n
    return float('inf')

N, b = int(input()), int(input())  # 이동하려는 채널, 고장난 버튼 개수
btn = list(map(int, input().split())) if b else 0 #  고장난 버튼
ch = 100  # 현재 채널

if N == ch : print(0)
elif not btn : print( min(len(str(N)), abs(100-N)) )
elif b == 10 : print(abs(100-N))
else :
    ch_m = ch_minus(N, ch, btn)
    ch_p = ch_plus(N, ch, btn, ch_m)
    ch_m, ch_p = abs(N-ch_m)+len(str(ch_m)), abs(N-ch_p)+len(str(ch_p))
    print( min(ch_m, ch_p, abs(100-N)) )




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

