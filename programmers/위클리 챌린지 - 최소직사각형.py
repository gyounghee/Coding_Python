# 가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다.
# 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다.
# 이때의 지갑 크기는 4000(=80 x 50)입니다.

# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성하라
 
# * 제한사항 *
# - sizes의 길이는 1 이상 10,000 이하입니다.
# - sizes의 원소는 [w, h] 형식입니다.

def solution(sizes):
    w, h = [],[]
    for n in sizes:
        w.append(n[0])
        h.append(n[1])
    answer = max(w) * max(h)
    
    for _ in range(len(sizes)):
        w_max_idx = w.index(max(w))
        w[w_max_idx], h[w_max_idx] = h[w_max_idx], w[w_max_idx]
        if max(w) * max(h) < answer :
            answer = max(w) * max(h)
    
    return answer


# TEST CASE Ⅰ
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(size))

# TEST CASE Ⅱ
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(size))

# TEST CASE Ⅲ
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(size))



# 다른 사람 풀이 Ⅰ
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# 다른 사람 풀이 Ⅱ
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)

## sum(sizes,[])  →  sizes의 모든 요소가 담긴 1차원 list로 변환해줌
