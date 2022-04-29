## 이것도 꼭 다시 풀어보기
## 직접 구현하지 못하고 다른 분의 풀이를 참고함ㅠ


# 왼쪽 자식 → 현재 인덱스*2
# 오른쪽 자식 → 현재 인덱스*2 + 1
def Tree(n) :
    global count

    if n <= N :
        # 왼쪽 자식 생성
        Tree(n * 2)
        # 왼쪽 자식 생성이 더 이상 불가능하면 노드 해당 인덱스에 노드 만들기
        tree[n] = count
        # 노드 생성 시 count + 1
        count += 1
        # 오른쪽 자식 생성
        Tree(n * 2 + 1)

count = int(input())

for c in range(1,count+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    count = 1
    Tree(1)
    
    print(f'#{c} {tree[1]} {tree[N//2]}')
    
