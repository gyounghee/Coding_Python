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
    return min(len(s_zip(s,zl)) for zl in range(1,len(s)+1))  # 압축할 문자 길이를 하나씩 늘려가며


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


## 다른 사람 풀이 
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
                                                    # 압축하려면 최소 같은 문자열이 2개 이상있어야 하므로 text길이에서 2를 나눠준 것 (내 풀이처럼 하나씩 다 늘려가며 할 필요 없음)
