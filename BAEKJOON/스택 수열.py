# 1874번 - 스택 수열

n = [ int(input()) for _ in range(int(input())) ]

s, ans = [], []
p = 0
for i in range(1,max(n)+1):
    s.append(i)
    ans.append('+')
    while s and s[-1] == n[p] :
        s.pop()
        ans.append('-')
        p += 1

if not s :
    for c in ans :
        print(c)
else :
    print('NO')
