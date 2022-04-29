# 수도 요금 경쟁

for c in range(int(input())):
    # A사 : P - 1L당 요금
    # B사 : R - 리터 /  Q - R리터 이하 요금 / S - 1L당 요금
    # W - 종민이가 한달 사용하는 수도 양
    P, Q, R, S, W = map(int, input().split())

    # A사 요금 계산
    A_cost = P * W

    # B사 요금 계산
    if W <= R : B_cost = Q
    else : B_cost = Q + (W-R) * S

    # 요금이 더 저렴한 회사 고르기
    if A_cost <= B_cost : low_cost = A_cost
    else : low_cost = B_cost

    print(f'#{c+1} {low_cost}')
