# 11727번 - 2×n 타일링 2
# - 메모리 : 30840 KB  /  시간 : 68 ms

n = int(input())
t = [0,1,3]
if n < 2 : print(t[n])
else :
    for i in range(3,n+1):
        t.append(t[i-1]+2*t[i-2])
    print(t[-1] %  10007)
