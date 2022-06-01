# 몫과 나머지 - divmod

a, b = map(int, input().strip().split(' '))
a, b = divmod(a,b)
print(a,b)


## 강의 풀이 - divmod, unpacking 이용
a, b = map(int, input().strip().split(' '))
print(*divmod(a,b))


# divmod를 사용할 때 주의할 점
#  - "divmode"는 작은 숫자를 다룰 때는 "a//b, a%b"보다 느리지만, 큰 숫자를 다룰 때는 용이
