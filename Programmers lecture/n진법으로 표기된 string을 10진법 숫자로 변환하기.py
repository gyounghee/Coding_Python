# n진법으로 표기된 string을 10진법 숫자로 변환하기

num, base = map(int, input().strip().split(' '))  # 숫자, 진법
print(int(str(num), base))


# python의 int()함수 → int(x, base=10)으로 진법 변환을 지원한다.


## 위 기능을 알지 못하면 보통 아래와 같은 방법으로 풀이
### - for문을 이용하여 숫자를 곱해가며 품
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
