# 내가 작성한 답안  -  답 틀림  
def solution(length, weight, trucks):
    time = length
    ing = []
    ed = []
    ing.append(trucks[0])
    time += 1
    for truck in trucks[1:] :
        if len(ing) < length :
            if (sum(ing)+truck) < weight :
                ing.append(truck)
                time += 1
            elif (sum(ing)+truck) == weight :
                ing.append(truck)
                time += 1
            elif (sum(ing)+truck) > weight :
                ed.append(ing.pop(0))
                ing.append(truck)
                time += 2
        else :
            ed.append(ing.pop(0))
            ing.append(truck)
            time += 1
    if len(ing) != 0 : time += length  
    return time
            


# TEST CASE Ⅰ
bridge_length, weight = 2, 10
truck_weights = [7, 4, 5, 6]
print( solution(bridge_length, weight, truck_weights) )

# TEST CASE Ⅱ
bridge_length, weight = 100, 100
truck_weights = [10]
print( solution(bridge_length, weight, truck_weights) )

# TEST CASE Ⅲ
bridge_length, weight = 100, 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print( solution(bridge_length, weight, truck_weights) )



# 다른 사람 풀이  - 코드 분석 해보기

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
