# 18870번 - 좌표 압축

## 내 풀이 
# - 메모리 : 156812 KB  /  시간 : 1956 ms

int(input())
n = list(map(int, input().split()))
nn = sorted(list(set(n)))

n_dict = {}
for i in range(len(nn)):
    n_dict[nn[i]] = i

for i in n :
    print(n_dict[i], end=' ')
