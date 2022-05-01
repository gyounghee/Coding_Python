### 클론 코딩 & 코드 분석 함 - 프로그래머스 제출 X (나중에 꼭 다시 풀어보기)
def solution(gems):
    find = len(set(gems))    # 찾고자 하는 보석의 개수
    if find == 1 :     # 찾고자 하는 보석이 1개인 경우 
        return [1,1]  

    left, right = 0,1     # left, right라는 두개의 포인터 사용
    answer = [1,len(gems)]
    
    data = dict()      # data라는 dictionary 생성
    data[gems[left]] = 1   # data에 gems[0]에 위치한 보석을 키로 설정하고 그에 대한 값을 1로 설정
    before = 0  
    while left < right :  # 앞부터 끝까지 둘러보기 위해 
        try :
            if before != right :  # 살펴볼 구간이 남아있다면
                data[gems[right]] += 1  
                before = right
        except KeyError :
            data[gems[right]] = 1
            before = right
        if len(data) == find and right-left < answer[1] - answer[0] :  # 만약 보석을 다 찾았고, answer보다 최단 구간일 경우
            answer = [left+1, right+1]    # answer 값을 변경

        # right가 gems의 길이보다 작고 보석을 다 찾지 못했으면,
        if right < len(gems)-1 and len(data) != find :
            right += 1   # right를 증가
        else :    # 더 탐색할 right가 없거나 보석을 다 찾았을 경우
            data[gems[left]] -= 1        #  data dictionary에서 gems[left] key에 해당하는 value -1 
            if data[gems[left]] == 0 :   #  data[gems]가 0이면 
                del data[gems[left]]     #  data dictionary에서 키 값 삭제
            left += 1   # 다음 순서 살펴보기 위해 left +1
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
