# Summer/Winter Coding(~2018) - 영어 끝말잇기

# 내 답안
from collections import defaultdict

def solution(n, words):
    word_dic = defaultdict(int)
    
    for i in range(len(words)):
        word_dic[words[i]] += 1
        if word_dic[words[i]] == 2 or i > 0 and words[i-1][-1] != words[i][0]:
            p_num = n if (i+1) % n == 0 else (i+1) % n
            order = (i+1) // n if (i+1) % n == 0 else ((i+1) // n) +1
            return [p_num, order]
    return [0,0]

