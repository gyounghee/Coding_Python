def solution(array):
    arr_dict = dict()
    answer = 0
    tmp = 0
    for i in array :
        try :
            arr_dict[i] += 1
        except :
            arr_dict[i] = 1
    
    max_num = max(arr_dict.values())
    for n in arr_dict:
        if arr_dict[n] == max_num:
            answer = n
            tmp += 1
        if tmp == 2 :
            return -1
    return answer

### 다른 사람 풀이 1
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1