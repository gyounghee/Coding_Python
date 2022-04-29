def rotation(array):
    for _ in range(len(array)):
        ary_rot = [i[::-1] for i in zip(*array)]
    return ary_rot

for c in range(int(input())):
    ary, answer = [], []
    for i in range(int(input())):   # 생성할 배열의 길이만큼
        ary.append(input().split())   # 한 줄 씩 추가

    ary_90 = rotation(ary)       # 90도
    ary_180 = rotation(ary_90)   # 180도
    ary_270 = rotation(ary_180)  # 270도

    answer.append([''.join(ary_90[i]) for i in range(len(ary))])
    answer.append([''.join(ary_180[i]) for i in range(len(ary))])
    answer.append([''.join(ary_270[i]) for i in range(len(ary))])
    
    print(f'#{c+1}')
    for i in range(len(ary)):
        for j in range(len(answer)):
            print(answer[j][i], end=' ')
        print()
