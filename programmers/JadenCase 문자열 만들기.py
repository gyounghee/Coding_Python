# JadenCase 문자열 만들기

def solution(s):
    st = s.split(' ')
    ans = []
    for i in range(len(st)) :
        if st[i] == '' : 
            ans.append('')
        elif st[i][0].isdigit() :
            ans.append(f'{st[i][0]}{st[i][1:].lower()}')
        else :
            ans.append(f'{st[i][0].upper()}{st[i][1:].lower()}')
        
    return ' '.join(ans)


# TEST CASE Ⅰ
s = " aaaaa aaa"
print(solution(s))    # " Aaaaa Aaa"

# TEST CASE Ⅱ
s = "a a a a a a a a a a "
print(solution(s))    # "A A A A A A A A A A "




## 다른 풀이 Ⅰ
# - capitalize() : 첫 글자만 대문자로 바꿔주는 함수
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])


## 다른 풀이 Ⅱ
#  ** 문제 개편 후에는 오답임 **
# - 내장함수 사용
def solution(s):
    return s.title()



#### upper()  /  capitalize()  /  title()  내장함수
## upper()
# - 주어진 문자열에서 모든 알파벳들을 대문자로 변환

## capitalize()
# - 주어진 문자열서 맨 첫글자를 대문자로 변환

## title()
# - 주어진 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 영단어들의 첫 글자를 모두 대문자로 변환시킴
