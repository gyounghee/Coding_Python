# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축
def s_zip(s,zl):
    i, duplicate = 0, '!'
    short = ""
    while i < len(s)-zl+1 :
        if s[i:i+zl] == s[i+zl:i+zl+zl] :
            i += zl
            try :
                duplicate += 1
            except :
                duplicate = 2
        else :
            short += f'{duplicate}{s[i:i+zl]}'
            duplicate = '!'
            i += zl
        if i >= len(s) -zl + 1 :
            short += s[i:]
            short = short.replace("!","")
            return short
        
def solution(s):
    zip_len = 9999
    for zl in range(1, len(s)+1): # 압축하려는 문자열을 하나씩 늘려가면서 
        tmp = len(s_zip(s, zl))
        if tmp <= zip_len :
            zip_len = tmp
    return zip_len



# TEST CASE Ⅰ
s = "aabbaccc"
print(solution(s))   # 7

# TEST CASE Ⅱ
s = "ababcdcdababcdcd"
print(solution(s))   # 9

# TEST CASE Ⅲ
s = "abcabcdede"
print(solution(s))   # 8

# TEST CASE Ⅳ
s = "abcabcabcabcdededededede"
print(solution(s))   # 14

# TEST CASE Ⅴ
s = "xababcdcdababcdcd" 
print(solution(s))   # 17

# TEST CASE Ⅵ
s = "aaaaaaaaaa" 
print(solution(s))   # 3
