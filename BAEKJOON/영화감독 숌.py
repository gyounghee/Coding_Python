# 1436번 - 영화감독 숌

n = int(input())

i = 0
cnt = 0   # # 666이 연속으로 몇번 나왔는 지
while True:
    i += 1
    if str(i).count("666") >= 1:
        title = i
        cnt += 1
    if cnt == n:
        break
    
print(title)
