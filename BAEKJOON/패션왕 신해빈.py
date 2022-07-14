# 9375번 - 패션왕 신해빈

## 내 풀이 
# - 메모리 : 32424 KB  /  시간 : 96 ms

# 아이디어 (다른 사람 아이디어 참고)
# - 옷을 입지 않는 부위를 "0 번째 옷을 입는다"라고 생각하여 품 
# ex) 옷의 종류 3개 각 종류의 개수 {2,3,4}라고 할 때,
#   - (2+1)*(3+1)*(4+1) -1 으로 풀이됨

from sys import stdin
from collections import defaultdict
from functools import reduce

input = stdin.readline
for tc in range(int(input())):
    cn = int(input())
    if cn == 0 :
        print(0)
        continue
    clothes = defaultdict(lambda : 1)
    ans = 0
    
    for _ in range(cn) :
        v, k = input().split()
        clothes[k] += 1
    c = list(clothes.values())
    
    print(reduce(lambda x, y : x*y, c) -1)
