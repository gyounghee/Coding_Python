# 월간 코드 챌린지 시즌 2 - 괄호 회전하기

def check(s) :
    stack = []
    s_dict = {'(':')', '{':'}', '[':']'}
    for c in s :
        try :
            if stack and s_dict[ stack[-1] ] == c :
                stack.pop()
            else :
                stack.append(c)
        except KeyError :
            stack.append(c)
    return len(stack)
    
def solution(s):
    from collections import Counter, deque
    
    answer = 0
    c = Counter(s)
    
    # 올바른 문자열 조건에 맞지 않으면 return 0
    if len(c) % 2 == 1 : return 0
    #### elif [ i for i in c.values() if i>2 and i % 2 == 1 ] : return 0
    
    # 올바른 문자열 체크
    s = deque(s)
    for _ in range(len(s)):
        if not check(s) : 
            answer += 1
        s.append(s.popleft())

    return answer

### * 실패 한 이유 
## elif [ i for i in c.values() if i>2 and i % 2 == 1 ] : return 0
## - 시간을 줄이기 위해 추가한 코드가 오류를 일으킴ㅜㅜ
## - 각 요소의 개수가 짝수 개로 이루어져야 올바른 문자열이라고 잘못 생각했음..(배가 고파서 머리가 안돌아갔나;;;)
