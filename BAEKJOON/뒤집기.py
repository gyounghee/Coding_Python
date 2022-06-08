def check(s):
    ans = 0
    for c in s :
        if len(c) :
            ans += 1
    return ans    

s = input()

s0, s1 = s.split('0'), s.split('1')
print( min(check(s0), check(s1)) )
