# 2812번 - 크게 만들기

n_len, del_n = map(int, input().split())
n = list(input())

p1, p2 = 0, 1
delete, trash = del_n, []
while p2 < n_len :
    if delete == 0 : break
    
    if len(trash) and trash[-1][1] > n[p2] :
        if trash[-1][0] < p1 :
            delete -= 1
            trash.append( (p2, n[p2]) )
            n[p2] = 'x'
            p2 += 1
        else :
            idx, val = trash.pop()
            n[idx] = val
            trash.append( (p2, n[p2]) )
            n[p2] = 'x'
            p2 += 1
    else :
        if n[p1] > n[p2] :
            delete -= 1
            trash.append( (p2, n[p2]) )
            n[p2] = 'x'
            p2 += 1 
        elif n[p1] < n[p2] :
            delete -= 1
            trash.append( (p1, n[p1]) )
            n[p1] = 'x'
            p1, p2 = p2, p2+1
        else :
            p1, p2 = p2, p2+1

while not delete and p2 < n_len and trash[-1][1] > n[p2]:
    idx, val = trash.pop()
    n[idx] = val
    trash.append( (p2, n[p2]) )
    n[p2] = 'x'
    p2 += 1

i = 0
while delete :
    if n_len == i : i = 0
    if n[i] < trash[-1][1] :
        idx, val = trash.pop()
        n[idx] = val
        trash.append( (i, n[i]) )
        n[i] = 'x'
    elif n[i] == trash[-1][1] or min(n) == n[i] :
        delete -= 1
        trash.append( (i,n[i]) )
        n[i] = 'x'
    i += 1

print( ''.join(i for i in n if i != 'x')[:(n_len-del_n)] )
