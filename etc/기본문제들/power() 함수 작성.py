# n이 주어졌을 때 2 ^ n을 구하는 함수 작성
# 2^n을 한 결과를 return값으로 한다.

count = int(input())
num = 1

for _ in range(count) :
    num *= 2

print(num)
