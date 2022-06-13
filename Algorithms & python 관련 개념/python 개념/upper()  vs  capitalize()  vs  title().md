#### upper()  /  capitalize()  /  title()  내장함수
## * **upper()**
# - 주어진 **문자열에서 모든 알파벳들**을 대문자로 변환
```python
s1 = 'abcd'
s1.upper()   # 'ABCD'

s2 = 'aAbB'
s2.upper()   # 'AABB'

s3 = 'a2b3c4' 
s3.upper()   # 'A2B3C4'

s4 = 'abc-def gh'
s4.upper()   # 'ABC-DEF GH'
```

## * **capitalize()**
# - 주어진 **문자열에서 맨 첫글자**를 대문자로 변환
```python
s1 = 'abcd'
s1.capitalize()   # 'Abcd'

s2 = 'aAbB'
s2.capitalize()   # 'Aabb'

s3 = 'a2b3c4' 
s3.capitalize()   # 'A2b3c4'

s4 = 'abc-def gh'
s4.capitalize()   # 'Abc-def gh'
```

## * **title()**
# - 주어진 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 **나누어져 있는 영단어들의 첫 글자**를 모두 대문자로 변환시킴
```python
s1 = 'abcd'
s1.title()   # 'Abcd'

s2 = 'aAbB'
s2.title()   # 'Aabb'

s3 = 'a2b3c4' 
s3.title()   # 'A2B3C4'

s4 = 'abc-def gh'
s4.title()   # 'Abc-Def Gh'
```