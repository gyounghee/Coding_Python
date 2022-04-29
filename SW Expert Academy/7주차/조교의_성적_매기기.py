for c in range(int(input())):
    S, SN = map(int, input().split()) # 학생 수, 학점을 알고 싶은 번호
    score,grade = [],['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

    for s in range(S) :  # 각 학생의 시험 점수 입력    
        m,f,hw = map(int, input().split()) # m - 중간, f - 기말, hw - 숙제
        score.append(round((m*0.35 + f*0.45 + hw*0.2),3))  # 평가 비율대로 계산해서 score에 추가

    find = score[SN-1]    # 학점을 알고싶은 학생 번호의 점수를 find에 놓고
    score.sort(reverse=True)   # 정렬을 하고
    find = score.index(find)  # 찾으려고했던 점수가 정렬했을 때 몇 번째에 있는지 find에 저장

    print(f'#{c+1} {grade[ find // (S//10) ]}')   
