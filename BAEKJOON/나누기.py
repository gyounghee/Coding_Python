# 1075번 - 나누기

## 내 풀이
# - 메모리 : 30840 KB  /  시간 : 68 ms

N, div = (int(input())//100)*100, int(input())
for n in range(N, 2000000000+99) :  # +1 이 아니라 +99를 해줬어야했음..
    if n % div == 0 :
        print(str(n)[-2:])
        break
