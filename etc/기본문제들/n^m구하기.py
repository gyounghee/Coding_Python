# n^m구하기

n, m = map(int, input().split())
num = n

if m == 0  : num = 1
elif m == 1 : pass
else : 
    for _ in range(2, m+1) :
        num *= n
print(num)
