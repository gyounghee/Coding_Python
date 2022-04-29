def u_check(p):
    while True :
        tmp_len = len(p)
        tmp = p.replace('()','')
        if len(tmp) == 0 : # 올바른 문자열 → check를 True로 하고 break해준다.
            return True     
        else tmp_len == len(tmp) :
            return False

def div_uv(p):
    L,R = 0,0
    for c in p :
        if c == '(' :
            L += 1
        elif c == ')' :
            R += 1
        if L == R :
            u = p[ : L+R ]
            v = p[ L+R : ]
            break
    return u,v

def solution(p):
    # check
    if check(p) :  # 입력된 문자열이 올바른 문자열이라면
        return p   # 바로 return
    else : # 입력된 문자열이 올바른 문자열이 아니라면
        u,v = div_uv(u,v)
        if check(u) == True and check(v) == False : 
        
            

    return u,v

# TEST CASE Ⅰ
p = "(()())()"
print(solution(p))

# TEST CASE Ⅱ
p = "()))((()"
print(solution(p))

# TEST CASE Ⅲ
p = "))()(("
print(solution(p))
