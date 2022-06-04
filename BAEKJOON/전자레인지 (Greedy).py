# 10162번 - 전자레인
# Greedy 알고리즘을 이용한 문제풀이

T = int(input())
button = [300, 60, 10]

for i in range(len(button)) :
    button[i], T = divmod(T, button[i])  

if T :
    print(-1)
else :
    print(button[0], button[1], button[2])

