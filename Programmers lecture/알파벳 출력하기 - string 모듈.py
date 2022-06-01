#  알파벳 출력하기 - string 모듈

num = int(input().strip())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet if num == 1 else alphabet.lower())




## 이번 강의에서는
# -  모든 대문자를
# - 또는 모든 소문자를
# - 또는 모든 대소문자를
# - 또는 숫자를
# 가져오는 방법을 배움

# 이 기능을 모르는 경우 alphabet = "AB ... YZ" 이런식으로 손수 입력함
# python에서는 이런 데이터를 상수(constants)로 정의해놓았음

import string

print(string.ascii_lowercase)   # 소문자
print(string.ascii_uppercase)   # 대문자
print(string.ascii_letters)     # 대소문자
print(string.digits)            # 숫자



## 이 밖에도 더 많은 string 상수 존재
### - https://docs.python.org/3.4/library/string.html
