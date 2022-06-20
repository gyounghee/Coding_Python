# 10869번 - 사칙연산

# 풀이 1
a, b = map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)


# 풀이 2
a, b = map(int,input().split())
print(a+b, a-b, a*b, a//b, a%b, sep='\n')
