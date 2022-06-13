# 9012번 - 괄

from sys import stdin

for _ in range(int(stdin.readline())) :
    s = stdin.readline().strip()
    stack = []
    for c in s :
        if not stack :
            stack.append(c)
        elif stack[-1] == '(' and c == ')' :
            stack.pop()
        else :
            stack.append(c)

    print('NO' if stack else 'YES')
