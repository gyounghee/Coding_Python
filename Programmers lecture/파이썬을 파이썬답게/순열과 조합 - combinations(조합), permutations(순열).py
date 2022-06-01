# 순열과 조합 - combinations(조합), permutations(순열)

from itertools import permutations 
def solution(mylist):
    p_list = permutations(mylist)  
    return sorted(p_list)


# python의 itertools.permutations을 이용
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 생성
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 생성
