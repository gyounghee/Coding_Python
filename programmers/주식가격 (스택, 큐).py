# 내 답안  -  스택 / 큐 사용하지 않은 풀이
def solution(prices):
    answer = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1,len(prices)):
            sec += 1
            if prices[i] > prices[j] : 
                break
        answer.append(sec)
    return answer

    
# TEST CASE Ⅰ
prices = [1,2,3,2,3]
print(solution(prices))   # [4,3,1,1,0]



## 스택을 이용한 풀이
def solution(prices):
    stack = []  
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer



## 스택을 이용한 풀이 2
def solution(p):
    ans = [0] * len(p)
    stack = [0]   # 주식 가격이 처음으로 떨어지는 지점을 못찾은 가격의 index 모음
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans
