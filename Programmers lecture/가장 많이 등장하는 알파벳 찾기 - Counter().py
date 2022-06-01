# 가장 많이 등장하는 알파벳 찾기 - collections.Counter()

from collections import defaultdict

my_str = input().strip()
dic = defaultdict(int)
answer = []

for s in my_str:
    dic[s] += 1

for k, v in dic.items() :
    if v == max(dic.values()) :
        answer += k
    
print(''.join(sorted(answer)))


# collections.Counter() 클래스 이용
# - 각 요소의 개수를 샌 것을 

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0

