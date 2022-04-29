# 초심자의 회문 검사

for c in range(int(input())):
    s = input()
    answer = 0
    if s == s[::-1] : answer = 1
    
    print(f'#{c+1} {answer}')
