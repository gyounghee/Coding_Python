clap_num = [3,6,9]    # 어떤 번호에 박수칠 것인지 

for n in range(1,int(input())+1):
    clap = 0  
    num = list(map(int, str(n)))  # 숫자를 하나씩 쪼개서 list로 만듦
    for i in range(len(num)):     # 리스트안의 요소들을 하나씩 봄
        if num[i] in clap_num : clap += 1  # 요소가 3,6,9 중 하나면 clap에서 해당 숫자 삭제
    if clap == 0 : print(n,end=' ')   # 3, 6, 9가 포함되지 않으면  숫자 그대로 출력
    else : print('-'* clap, end=' ')   # 3,6,9가 포함되면 포함된 수만큼 '-'출력
