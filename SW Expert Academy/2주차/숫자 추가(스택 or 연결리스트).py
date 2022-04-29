# 숫자 추가(스택 or 연결리스트) → 5차시 숫자 추
count = int(input())

for i in range(1,count+1):
    #  N - 수열의 길이 /  M - 추가 횟수  /  L - 출력할 인덱스 번호
    N, M , L = map(int, input().split())
    seq = input().split()    # 수열 입력
    for _ in range(M) :     # M(추가 횟수) 만큼 반복
        loc, num =  map(int, input().split())    # 추가할 위치, 추가할 숫자
        seq.insert(loc,num)
    print(f'#{i} {int(seq[L])}')
