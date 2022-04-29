# KAKAO BLIND RECRUITMENT - 오픈채팅방

# 카카오톡 오픈채팅방에서는 친구가 아닌 사람들과 대화를 할 수 있는데,본래 닉네임이 아닌 가상의 닉네임을 사용하여 채팅방에 들어갈 수 있다.
# 신입사원인 김크루는 카카오톡 오픈 채팅방을 개설한 사람을 위해, 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창을 만들기로 했다.

# * 채팅방에 누군가 들어오면 다음 메시지가 출력된다.
# → "[닉네임]님이 들어왔습니다."

# * 채팅방에서 누군가 나가면 다음 메시지가 출력된다.
# → "[닉네임]님이 나갔습니다."

# * 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
# → 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# → 채팅방에서 닉네임을 변경한다.
# → 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.


# ** 제한사항 **
# record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
# 다음은 record에 담긴 문자열에 대한 설명이다.
# 모든 유저는 [유저 아이디]로 구분한다.
# [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
# [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
# [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
# 첫 단어는 Enter, Leave, Change 중 하나이다.
# 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
# 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
# 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
# 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.



def solution(record):
    answer = []
    nickname_dict = {}
    for words in record:
        if len(words.split()) > 2 :
            user_id = words.split()[1]
            nickname = words.split()[2]
            nickname_dict[user_id] = nickname
        
    for words in record:
        word = words.split()
        if word[0] == "Enter" : 
            answer.append(f'{nickname_dict[word[1]]}님이 들어왔습니다.')
        elif word[0] == "Leave" :
            answer.append(f'{nickname_dict[word[1]]}님이 나갔습니다.')
            
    return answer


# TEST CASE Ⅰ
# 결과값 → ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
