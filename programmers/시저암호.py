# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 한다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 된다,
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성하라

def solution(s, n):
    answer = ""
    for i in range(len(s)):
        if ord(s[i]) == 32 : answer += s[i]
        else :
            if ord(s[i]) >=65 and ord(s[i]) <= 90 :
                if ord(s[i])+n > 90 : answer += chr(ord(s[i])+n-26) 
                else : answer += chr(ord(s[i])+n)
            elif ord(s[i]) >=97 and ord(s[i]) <= 122 :
                if ord(s[i])+n > 122 : answer += chr(ord(s[i])+n-26)   
                else : answer += chr(ord(s[i])+n)
    return answer


# TEST CASE Ⅰ   →  "BC"
s, n = "AB" , 1
solution(s,n)

# TEST CASE Ⅰ   →  "a"
s, n = "z" , 1
solution(s,n)

# TEST CASE Ⅰ   →  "e F d"
s, n = "a B z" , 4
solution(s,n)

# TEST CASE Ⅰ   →  "ZzYy"
s, n = "AaZz" , 25
solution(s,n)



# 다른 사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
