# 문자열 s는 한 개 이상의 단어로 구성
# 각 단어는 하나 이상의 공백문자로 구분
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하라

# ** 제한 사항 **
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.


def solution(s):
    answer = ''
    i, idx = 0, 0
    while True :
        if i+idx == len(s) :
            break
        if s[idx+i] == ' ':
            answer += ' '
            idx, i = idx+i+1, 0
        else :
            if i % 2 == 0 :
                answer += s[idx+i].upper()
                i += 1
            else : 
                answer += s[idx+i].lower()
                i += 1
    return answer

# TEST CASE Ⅰ
s = "try hello world"
print(solution(s))    # "TrY HeLlO WoRlD"

