### 바보 코드
def solution(operations):
    num_list = []
    operations_list = list(map( lambda e : e.split(' ') , operations))
    for c, n in operations_list :
        if c == 'I' :
            num_list.append(int(n))
        else :
            if n == '1' and len(num_list):
                max_idx = num_list.index(max(num_list))
                num_list.pop(max_idx)
            elif n == '-1' and len(num_list) :
                min_idx = num_list.index(min(num_list))
                num_list.pop(min_idx)
    return [0,0] if len(num_list) == 0 else [max(num_list), min(num_list)]

## 덜 바보 코드..?
import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    num_list = []
    operations_list = list(map( lambda e : e.split(' ') , operations))
    for c, n in operations_list :
        if c == 'I' :
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
        else :
            if n == '1' and len(max_heap):
                heapq.heappop(max_heap)
            elif n == '-1' and len(min_heap) :
                heapq.heappop(min_heap)

    if len(min_heap) > 1 :
        for n in max_heap :
            if -n in min_heap :
                num_list.append(-n)

    return [max(num_list), min(num_list)] if len(num_list) >1 else [0,0]



## 힙(Heap)
# '완전 이진 트리' 의 일종으로 우선순위 큐를 위하여 만들어진 자료구조
# ...