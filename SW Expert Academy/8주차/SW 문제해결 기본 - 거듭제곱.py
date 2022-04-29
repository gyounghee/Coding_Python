def power(N,M):
    if M < 1 : return 1
    else : return N * power(N,M-1)

for _ in range(10):
    c = int(input())
    N, M = map(int, input().split())
    print(f"#{c} {power(N,M)}")
