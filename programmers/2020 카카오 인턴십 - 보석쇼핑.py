### 푸는 
def solution(gems):
    answer = []
    f_gems = list(set(gems))   # 찾고자 하는 보석

    # 보석 data의 정보를 dict형식으로
    gem_dict = dict.fromkeys(gems)
    for gem in f_gems :
        gem_dict[gem] = gems.count(gem)


    # 보석 구간 찾기
    if len(gem_dict.keys()) == 1 :  # 보석의 종류가 1개인 경우
        return [1,1]
    elif len(gem_dict.keys()) == sum(gem_dict.values()):  # 여러 보석이 각각 1개 씩 있는 경우
        return [1,len(gems)]
    
    return answer


# TEST CASE Ⅰ
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))   # [3, 7]

# TEST CASE Ⅱ
gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))   # [1, 3]

# TEST CASE Ⅱ
gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))   # [1, 1]

# TEST CASE Ⅱ
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))   # [1, 5]
