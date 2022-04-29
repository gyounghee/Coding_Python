import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K :
        if len(scoville) == 1 : return -1
        else : 
            first =  heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
            answer += 1
    return answer


# TEST CASE Ⅰ
scoville, K = [0,0,2], 2 
print(solution(scoville, K))
