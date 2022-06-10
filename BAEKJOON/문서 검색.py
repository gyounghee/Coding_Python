# 1543번 - 문서 검색

s, f = input().replace(' ','.'), input().replace(' ','.')

l, ans = 0, 0
for r in range(1,len(s)+1) :
    if f in s[l:r] :
        l = r
        ans += 1

print(ans)

## 다른 풀이
print(input().count(input()))
