# 4344번 - 평균은 넘겠지

# 이슈 : round를 이용하여 소수점 자리가 3자리까지 표현되지 않을 경우를 고려하지 못하여 틀림
#  →  f-string을 사용하여 소수점 자리수를 지정하여 표현

from sys import stdin 

for tc in range(int(stdin.readline())):
    C = list(map(int, stdin.readline().split()))

    score = C[1:]
    score.sort(reverse = True)
    avg = sum(score)/C[0]

    for i in range(C[0]):
        if score[i] <= avg :  break

    print( f'{i/C[0]*100:.3f}%' if i != 0 else '0.000%')
