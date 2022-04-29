for c in range(1,11):    # 총 10개의 TEST CASE
    carry = int(input())       # 반복할 횟수  
    box = input().split()      # 상자의 높이들 입력받음
    box = list(map(int, box))  # str형태의 요소들을 int로 형변환

    for _ in range(carry):
        max_idx, min_idx = box.index(max(box)), box.index(min(box))  # 가장 큰 높이와 가장 작은 높이 박스의 위치 저장
        box[max_idx] -= 1   # 가장 높은 박스의 높이는 -1 해주고
        box[min_idx] += 1   # 가장 낮은 박스의 높이는 +1 해준다

    print(f'#{c} {max(box) - min(box)}')
