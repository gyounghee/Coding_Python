# for문과 if문을 한번에 - List comprehension의 if문

def solution(mylist):
    return [(i**2) for i in mylist if i % 2 == 0]



## 리스트 컴프리헨션(list comprehension)
### - 'list를 쉽게, 짧게 한 줄로 만들 수 있는 python의 문법'
### - list, set, dict 구조를 생성할 때도 사용 가능
### - 그러나 tuple을 생성하기 위해서는 앞에 tuple 자료 구조임을 명시해주어야 한다
####  - (n for n in range(1, 10))   →  이 식은 generator를 생성하는 generator comprehension 
####  - tuple(n for n in range(1, 10))  →  comprehension으로 tuple을 생성


## 1. list comprehension의 if문 "AND 조건"
###  - 아래와 같이 두 if문 사이에 "and"를 사용하지 않고 조건문을 나열
###  - 명시적으로  "and" 를 사용할 경우 SyntaxError 발생
arr = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]



## 2. list comprehension의 if문 "OR 조건"
###  - 다중 if 조건문에 대해 or연산은 불가능, 명시적으로 "or"를 사용할 경우 SyntaxError 발생
###  - if문을 여러개 사용하지 않고, 한 if문에서 "or" 연산자로 논리 연산을 묶어줘야 함
arr = [n for n in range(1, 16) if n % 2 == 0 or n % 3 == 0]
