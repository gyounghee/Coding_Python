### 클론 코딩 & 코드 분석 함 - 프로그래머스 제출 X (나중에 꼭 다시 풀어보기)
def solution(gems):
    find = len(set(gems))   # 찾고자 하는 보석
    if find == 1 :  # 보석의 종류가 1개인 경우 
        return [1,1]

    left, right = 0,1
    answer = [1,len(gems)]
    data = dict()
    data[gems[left]] = 1
    before = 0
    while left < right :
        try :
            if before != right :
                data[gems[right]] += 1
                before = right
        except KeyError :
            data[gems[right]] = 1
            before = right
        if len(data) == find and right-left < answer[1] - answer[0] :  # 만약 data의 길이와 찾으려는 길이가 같고, ~~ 면
            answer = [left+1, right+1]
        if right < len(gems)-1 and len(data) != find :
            right += 1
        else :
            data[gems[left]] -= 1
            if data[gems[left]] == 0 :
                del data[gems[left]]
            left += 1
    return answer


# TEST CASE Ⅰ
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))   # [3, 7]

# TEST CASE Ⅱ
gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))   # [1, 3]

# TEST CASE Ⅲ
gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))   # [1, 1]

# TEST CASE Ⅳ
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))   # [1, 5]

# TEST CASE Ⅴ
gems = ["A","A","A","B","B"] 
print(solution(gems))   # [3,4]

# TEST CASE Ⅵ
gems = ["A","B","B","B","B","B","B","C","B","A"]  
print(solution(gems))   # [8,10]
