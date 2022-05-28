# 피로도
 
# 내 답안 - 조합, 완전 탐색 이용
from itertools import permutations  # 조합 사용하기 위해

def solution(k, dungeons):
    p_list = list(range(len(dungeons)))
    p = list(permutations( p_list , len(dungeons)))
    max_adv = 0
    
    for p_nums in p :
        tmp_k, adv = k, 0
        for p_num in p_nums :
            if tmp_k >= dungeons[p_num][0] :  # 최소 필요 피로도가 현재 피로도보다 크거나 같으면
                tmp_k -= dungeons[p_num][1] 
                adv  += 1
            else : break
        if adv >= max_adv :
            max_adv = adv
    return max_adv
