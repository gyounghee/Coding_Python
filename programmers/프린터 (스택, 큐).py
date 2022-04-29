# 프린터 (스택/ 큐)

# * 동작 방법 *
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼낸다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣는다.
# 3. 그렇지 않으면 J를 인쇄한다.
# → 예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고
#    중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 된다

# * 제한사항 *
# - 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
# - 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
# - location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.




def solution(priorities, location):
    box = []
    loc_num = [i for i in range(len(priorities))]
    while True:
        if priorities[0] != max(priorities):
            priorities.append( priorities.pop(0) )
            loc_num.append(loc_num.pop(0))
        else :
            if loc_num[0] == location :
                box.append(loc_num.pop(0))
            else :
                priorities.pop(0)
                box.append(loc_num.pop(0))
        if location in box : break
    return len(box)

# TEST CASE Ⅰ
priorities = [2, 1, 3, 2]  # 문서의 중요도가 순서대로 담긴 배열
location = 2  # 내가 인쇄를 요청한 문서가 현재 대기목록에 있는 위치
print(solution(priorities, location)) # return 1 
# TEST CASE Ⅱ
priorities = [1, 1, 9, 1, 1, 1, 1]
location = 0
print(solution(priorities, location)) # return 5
