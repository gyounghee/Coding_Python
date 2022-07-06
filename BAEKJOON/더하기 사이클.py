# 1110번 - 더하기 사이클

# 내 풀이
N = input()
count = 1

tmp = N[-1]+str(sum(map(int, list(str(N)))))[-1] 

while int(tmp) != int(N) :
    tmp = tmp[-1]+str(sum(map(int, list(tmp))))[-1]
    count += 1

print(count)


# 다른 사람 풀이

N = int(input())
tmp = N
c = 0

while True:
    tmp = tmp % 10 * 10 + (tmp % 10 + tmp // 10) % 10
    c += 1
    if tmp == N:
        break
print(c)
