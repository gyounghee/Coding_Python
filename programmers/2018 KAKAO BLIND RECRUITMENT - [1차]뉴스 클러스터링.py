def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()  # 문자를 대문자로 통일
    
    # 2글자씩 끊어서 list로 만듦
    str1_list = [ str1[i:i+2] for i in range(0, len(str1)-1, 1) ]  
    str2_list = [ str2[i:i+2] for i in range(0, len(str2)-1, 1) ]

    # 제대로 된 원소만 남기기 (중복 제거)
    str1_list = [ s for s in str1_list if s.isalpha()]
    str2_list = [ s for s in str2_list if s.isalpha()]

    list1_copy = str1_list.copy()
    list2_copy = str2_list.copy()

    # 교집합 
    inter = []
    for i in str1_list:
        if i in list2_copy:
            inter.append(i)
            list1_copy.remove(i)
            list2_copy.remove(i)

    union = len(str1_list) + len(str2_list) - len(inter)
    inter = len(inter)
    
    if union == 0 : 
        return 65536
    answer = int( inter / union * 65536 )
    return answer


# TEST CASE Ⅰ
str1 = "FRANCE"
str2 = "french"
print(solution(str1,str2))

# TEST CASE Ⅱ
str1 = "handshake"
str2 = "shake hands"

# TEST CASE Ⅲ
str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1,str2))

# TEST CASE Ⅳ
str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(solution(str1,str2))

# TEST CASE Ⅴ
str1 = "aa1+aa2"
str2 = "AA12"
print(solution(str1,str2))     # 32768




### 교집합 구할 때 이슈

## 1
# 중복인 원소가 있을 경우 적합하지 않음을 인지
# union_len = k for k,v in e_dict.items()]  # 합집합 원소 개수
# inter_len = [k for k,v in e_dict.items() if v >= 2 ]  # 교집합 원소 개수

## 2
# 이 방법 또한 교집합을 찾는데 적절한 방법이 아님을 인지
# inter1 = [s for s in str1_list if s in str2_list]  # str1_list를 기준으로 교집합
# inter2 = [s for s in str2_list if s in str1_list]
# inter = min(len(inter1), len(inter2))  # 더 작은 것을 교집합으로 간주





## 다른 사람 풀이

import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
