# 1092번 - 배

# 시간 초과
N, w = int(input()), list(map(int, input().split()))
M, b = int(input()), list(map(int, input().split()))

ans = 0
w.sort(reverse=True)
b.sort(reverse=True)

if max(w) < max(b) : print(-1)
elif min(w) >= max(b) :
    print(M//2 if M%2 == 0 else M//2+1)
else :
    while b :
        ans += 1
        for cw in w :
            for bw in b :
                if cw >= bw :
                    b.pop(b.index(bw))
                    break
    print(ans) 
