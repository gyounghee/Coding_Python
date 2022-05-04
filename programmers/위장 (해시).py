from functools import reduce

def solution(clothes):
    clothes_type = list(set([c[1] for c in clothes]))
    clothes_dict = dict.fromkeys(clothes_type, 1)
    for ct in clothes:
        clothes_dict[ct[1]] +=1
    
    if len(clothes_type) == 1 :  # 옷 종류가 하나 일 때 
        return len(clothes)
    else :
        return reduce(lambda x, y : x * y, clothes_dict.values()) - 1


# TEST CASE Ⅰ
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

# TEST CASE Ⅱ
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
