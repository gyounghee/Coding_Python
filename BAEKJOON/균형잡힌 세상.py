# 4949번 - 균형잡힌 세상

## 1번 풀이
import re
from sys import *
input = stdin.readline

while True :
    s = input().rstrip()
    if s == '.' : break

    s = re.sub(r'[A-Za-z.]', '',s).replace(' ','')    # 괄호만 걸러냄
    door = {'[':']', '(':')'}
    stack = []
    
    for d in s :
        try : 
            if stack and door[stack[-1]] == d :
                stack.pop()
            else :
                stack.append(d)
        except :
            stack.append(d)
            
    if not stack : print('yes')
    else : print('no')



## 2번 풀이
# - 1번 풀이와 풀이 시간은 동일하지만, 메모리 사용량과 코드 길이가 적음
import re
from sys import *
input = stdin.readline

while True :
    s = input().rstrip()
    if s == '.' : break

    s = re.sub(r'[A-Za-z.]', '',s).replace(' ','')    # 괄호만 걸러냄
    stack = []
    
    for d in s :
        if stack and ((d == ')' and stack[-1] == '(') or (d == ']' and stack[-1] == '[')) :
            stack.pop()
        else :
            stack.append(d)

    if not stack : print('yes')
    else : print('no')
