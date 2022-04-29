# 2017 팁스타운 - 짝지어 제거하기

# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작한다
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾는다
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙인다
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료된다
# 문자열을 모두 제거할 수 있으면 1을 반환, 그렇지 않으면 0을 반환한다.


# 내 답안   -  정확성, 효울성 모두 통과 :)
def check(box):
    if box[-1] == box[-2] :
        box.pop(-1)
        box.pop(-1)
    return box

def solution(s):
    box = []

    for i in range(len(s)):
        box.append(s[i])
        if len(box) > 1 : check(box)

    if len(box) == 0 : return 1
    else : return 0
    


# TEST CASE Ⅰ    →  1 
s = 'baabaa' 
print(solution(s))

# TEST CASE Ⅱ    → 0
s = 'cdcd'
print(solution(s))
