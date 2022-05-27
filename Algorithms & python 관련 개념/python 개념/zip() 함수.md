## **zip()**
#### - python의 내장 함수

* zip() 함수 
	- zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고있는 원소의 tuple 형태로 차례로 접근할 수 있는 iterator를 반환
	- 양쪽의 data를 하나씩 차례로 짝 지어주는 역할

1. zip() 기본 사용법
```pyton
n = [10, 11, 12]
c = ["C","D","E"]

for piar in zip(n, c):
	print(pair)

# 결과
# (10, "C")
# (11, "D")
# (12, "E")
```

2. zip()함수로 병렬처리
	- zip()함수를 이용해 여러 그룹의 데이터를 한번에 루프로 처리
```python
for num, upper, lower in zip("123", "ABC", "abc") :
	print(num, upper, lower)

# 결과
# 1 A a
# 2 B b
# 3 C c
# 4 D d
# 5 E e
```

3. unzip
	- zip()함수로 엮어 놓은 data를 해체(unzip)하고 싶을 때, *(unpacking) 연산자를 붙여 zip 함수에 넣기면 됨
```python
numbers = (1, 2, 3)
letters = ("A", "B", "C")

# zip()이용하여 packing
paris = list(zip(numbers, letters))

# paris  출력 결과
# [(1, "A"), (2, "B"), (3, "C")]

# unpacking
numbers, letters = zip(*pairs)

# numbers 출력 결과
# (1, 2, 3)
# letters 출력 결과
# ("A", "B", "C")
```

4. 사전 변환
	- zip() 함수를 이용하여 두개의 list 또는 tuple로부터 dictionary 를 만들 수 있음
```python
month = [3, 4, 5]
day = [31, 30, 31]
dic = dict(zip(month, day))

# dic 출력 결과
# { 3 : 31, 4 : 30, 5 : 31 }
```

4. 주의 사항
	- zip() 함수로 넘기는 인자의 길이가 다를 때는 주의
	- **가장 짧은 인자를 기준으로 data가 엮이고, 나머지는 버려짐**
``` python
numbers = [1, 2, 3]
letters = ["A"]

list(zip(numbers, letters))
# 출력 결과
# [(1,"A")]
```


