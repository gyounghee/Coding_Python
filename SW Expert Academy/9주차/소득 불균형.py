for tc in range(int(input())):
    person = int(input())
    p_cost = list(map(int, input().split()))
    avg, count = sum(p_cost)/person, 0
    
    p_cost.sort()  # 한번 정렬해주고

    for i in range(len(p_cost)):
        if p_cost[i] > avg : break
        else : count += 1

    print(f"#{tc+1} {count}")
