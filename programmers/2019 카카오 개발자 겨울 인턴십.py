# 2019 카카오 개발자 겨울 인터십

def solution(s):
    s = ( s.replace('},{','split').replace('{','').replace('}','') ).split('split')
    
    sorted_s = sorted(s, key=len) 
    for n in range(len(sorted_s)):
        sorted_s[n] = sorted_s[n].split(',')
                                              
    num_list = sum(sorted_s,[])               
    num_list = list(dict.fromkeys(num_list))  
    
    answer = list(map(int, num_list))
    return answer


# TEST CASE Ⅰ
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))   # [2, 1, 3, 4]

# TEST CASE Ⅱ
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))   # [2, 1, 3, 4]

# TEST CASE Ⅲ
s = "{{20,111},{111}}"
print(solution(s))   # [111, 20]

# TEST CASE Ⅳ
s = "{{123}}"
print(solution(s))   # [123]

# TEST CASE Ⅴ 
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))   # [3, 2, 4, 1]


## 다른 풀이
def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))
    answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer

# -----------------------------------------------------------------------
## eval 함수
## : 문자열로 식을 입력하면 해당식을 실행한 결과값을 반환해 주는 함수

## eval 함수에 대해 검색을 해보면 사용을 조심해야한다는 내용들이 많이 적혀져있는데 왜 그럴까?
### 1. eval함수는 해당 표현식을 그대로 실행하는 것이기 때문에 Command Inejction Flaws를 그대로 노출할 수 있음
### 2. eval() 명령은 코드의 가독성을 떨어뜨리고 디버깅을 어렵게 만들 수 있음
### 3. 또한 eval을 사용해 일부 로컬 환경에 의존하도록 구현할 경우 환경 의존성도 생길 수 있으므로 되도록 사용하지 않길 권장함

## 추가로, ast module에 안전한 eval을 제공하는 "literal_eval"이라는 것이 있음
### eval은 built-in(내장함수)이지만 literal_eval은  AST module에서 제공하는 함수 중 하나
### AST(Abstract Syntax Trees) module은 문법을 구조화 시켜주는 모듈임
### literal_eval은 literal evaluate를 실행하는 함수 즉, python에서 제공하는 기본 type 정도만 변환해주는 용도로 사용 가능
