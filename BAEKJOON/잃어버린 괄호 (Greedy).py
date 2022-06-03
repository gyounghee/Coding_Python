f = input()

open_P = 0     # 괄호(Parenthesis)
add_n, minus_n  = '', ''
total = 0
for i in range(len(f)) :
    if (i == 0 and f[i] == '0') or ( f[i-1] in ['+'] and f[i] == '0'):
        continue
    
    if not open_P and f[i] == '-' :  # 괄호가 닫힌 상태에서 '-' 만나면 
        open_P = 1                     # 괄호를 열음
    elif open_P and f[i] == '-' :   # 괄호가 열린 상태에서 '-' 만나면
        minus_n = minus_n.split('+')
        if '' in minus_n  :  minus_n.remove('')
        add_n = add_n.split('+')
        if '' in add_n :  add_n.remove('')
        total += sum(list(map(int, add_n))) - sum(list(map(int, minus_n))) 
        add_n, minus_n = '', ''
    elif open_P  :              # 괄호가 열려있는 경우
        minus_n += f[i]      #  minus_n에 추가
    else :
        add_n += f[i]        # add_n에 추가

if len(minus_n) :   # 계산 후 minus_n에 숫자가 있으면 (괄호를 연 후 마지막까지 '-'를 만나지 못했을 경우)
    minus_n = minus_n.split('+')
    if '' in minus_n :  minus_n.remove('')
    add_n = add_n.split('+')
    if '' in add_n :  add_n.remove('')
    total += sum(list(map(int, add_n))) - sum(list(map(int, minus_n))) 
    print(total)
else :
    add_n = add_n.split('+')
    if '' in add_n :  add_n.remove('')
    total += sum(list(map(int, add_n)))
    print(total)
