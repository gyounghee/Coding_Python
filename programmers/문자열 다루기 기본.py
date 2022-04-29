# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True

def solution(s):
    if len(s) in [4,6] and s.isdigit():
        return True
    else : 
        return False

# TEST CASE Ⅰ
s = "a234"
print(solution(s))   # False


# TEST CASE Ⅱ
s = "1234"
print(solution(s))   # True
