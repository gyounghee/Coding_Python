## 풀이 2 - 풀이1 개선
# - 수행시간은 풀이 1과 동일
f = input()
P = 0     # 괄호(Parenthesis)
add_n, minus_n  = '', ''

for i in range(len(f)) :
    if not P and f[i] == '-' :  # 괄호가 닫힌 상태에서 '-' 만나면 
        P = 1                   # 괄호를 열음
    elif P and f[i] == '-' :    # 괄호가 열린 상태에서 '-' 만나면
        minus_n += '+'
    elif P  :                   # 괄호가 열려있는 경우
        minus_n += f[i]         #  minus_n에 추가
    else :
        add_n += f[i]           # add_n에 추가

minus_n = sum( list(map(int, minus_n.split('+'))) ) if len(minus_n) else 0
add_n =  sum( list(map(int, add_n.split('+'))) ) if len(add_n) else 0
print(add_n - minus_n)



## 다른 사람 풀이
# - 입력 받은 것을 먼저 '-'를 구분자로 하여 나눈 후 거기서 또 '+'를 구분자로 하여 나눈다.
# - 그럼 첫 번째 원소만 +인자를 가진 원소가 될 것이기 때문에
# - 첫 번째 원소에서 첫 번째 원소 이후 모든 값의 합을 빼주면 최소값이 됨
e = [sum(map(int, x.split('+'))) for x in input().split('-')] 
print(e[0]-sum(e[1:]))









## 풀이 1
# - 코드가 매우 더러워서 창피하다
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
