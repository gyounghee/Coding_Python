# 두 개의 숫자열

# TEST CASE Ⅰ
# 3 5
# 1 5 3
# 3 6 -7 5 4

for c in range(int(input())):
    N, M = map(int, input().split()) # N - 리스트A 길이 / M - 리스트B 길이
    A = input().split()
    B = input().split()

    # 길이가 긴 list를 long,  길이가 짧은 list를 short라고 지정
    if len(A) >= len(B) : long, short = A, B   
    else : long, short = B, A

    # "long-short+1번" 만큼 반복하니까 그 만큼의 길이를 가진 list 생성
    total_list = [0] * (len(long)-len(short)+1)  
    
    for i in range( len(total_list) ): 
        total = 0    # 한 번 돌 때마다 합을 계산해줄 total 변수 생성
        for j in range(len(short)):  
            total += int(short[j]) * int(long[j+i])
        total_list[i] = total   
    print(f'#{c+1} {max(total_list)}')  # total_list 요소 중 가장 큰 요소 출력
