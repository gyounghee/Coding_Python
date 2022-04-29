count = int(input())

for c in range(1, count+1) :
    str_input = input()          # 문자 입력받음 
    str_list = list(str_input)   # 입력받은 문자 쪼개서 리스트에 저장
    str_stack = []               # 빈 스택 생성 
    for i in str_list :          # i에 문자를 하나 씩 삽입하며 반복
        str_stack.append(i)      # 스택에 문자 삽입
        for k in range(len(str_stack)-1):         # 스택안의 요소를 확인하기 위한 반복문
            if str_stack[k] == str_stack[k+1] :   # 만약에 앞, 뒤로 요소가 겹친다면
                del str_stack[k+1]         # 삭제
                del str_stack[k]           # 삭제
    print(f'#{c} {len(str_stack)}')   # 스택에 남아있는 요소 개수 출력
