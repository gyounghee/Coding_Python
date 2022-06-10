def check(s):
    ans = 0
    for c in s :
        if len(c) :
            ans += 1
    return ans    

s = input()

s0, s1 = s.split('0'), s.split('1')
print( min(check(s0), check(s1)) )


## 다른 사람 풀이
change = 0
prev = '?'
string = input()
for i in string:
    if i != prev : change += 1
    prev = i
print(change//2)
