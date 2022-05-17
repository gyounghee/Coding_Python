from collections import deque

ans = deque([])
for _ in range( int(input()) ):
    c = input().split() 
    if c[0] == 'push':
        ans.append(int(c[1]))
    elif c[0] == 'pop':
        if len(ans) == 0 : print(-1)
        else :  print(ans.popleft())
    elif c[0] == 'size':
        print(len(ans))
    elif c[0] == 'empty':
        if len(ans) == 0 : print(1)
        else :  print(0)
    elif c[0] == 'front' :
        if len(ans) == 0 : print(-1)
        else :  print(ans[0])
    elif c[0] == 'back' :
        if len(ans) == 0 : print(-1)
        else :  print(ans[-1])
