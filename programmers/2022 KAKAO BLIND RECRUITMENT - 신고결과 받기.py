# 2022 KAKAO BLIND RECRUITMENT - 신고결과 받기

# 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템 개발
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

# 이용자의 ID가 담긴 문자열 배열 id_list,
# 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report,
# 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때,
# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 작성하라



# 나의 풀이
def solution(id_list, report, k):
    answer = []
    stop = []   # 정지된 사용자 
    attacker,mail = {},{}  # 어떤 유저가 몇 번 신고를 받았는지  |  어떤 유저에게 몇 번 이메일을 보낼 것인지
    report = list(set(report))  # 중복 제거 - 동일한 유저에 대한 신고 횟수를 1회로 처리하기 한 것
    for u in id_list:  # 가해자에 대한 정보를 담기 위한 dict, mail을 보내기 위한 dict 생성 
        attacker[u],mail[u] = 0,0    # 각 유저 아이디별로 key 값을 설정하고 초기 value값은 0으로 설정

    for i in range(len(report)):      # report에서 신고자와 피신고자를 분리하기 위함
        attack_user = report[i].split()[1]    # report에는 피신고자만 뽑아서 남겨놓음
        attacker[attack_user] += 1    # 신고당한 사람의 value 값 +1 씩 높여줌
    
    for key, value in attacker.items() :  # 가해자 목록을 살펴봄
        if value >= k :    # 정지 기준 신고 횟수를 넘으면 
            stop.append(key)         # 정지 ID 목록에 ID 추가
    
    for i in range(len(report)):
        if report[i].split()[1] in stop :    # 신고당한 사람이 정지 id 목록에 있으면
            mail[report[i].split()[0]] += 1  # 신고한 사람의 value 값 +1
            
    for i in mail.values():
        answer.append(i)
    
    return answer

# TEST CASE Ⅰ   → 결과값 : [2,1,1,0]
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

# TEST CASE Ⅱ   → 결과값 : [0,0]
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))




# ---------------------------------------------------------------------------------
# 다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
