for c in range(int(input())):
    num = list(map(int, input().split()))

    num.remove(max(num))  # 최대값 삭제
    num.remove(min(num))  # 최솟값 삭제

    print(f'#{c+1} { int(round(sum(num)/len(num),0))}')  # 평균구하고 첫째 자리에서 반올림 한 정수 출력
