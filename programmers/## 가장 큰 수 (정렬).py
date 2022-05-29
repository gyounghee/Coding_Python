# TEST CASE  1 ~ 6 실패 - 시간초과
#  문제인지 : permutations을 사용 - 비효율적인 코드

def find_max(num_list):
    from itertools import permutations
    p_list = list(permutations(num_list,len(num_list)))
    p_list = list(map(int, [''.join(n) for n in p_list]))
    return str(max(p_list))
    
def solution(numbers):
    if sum(numbers) == 0 :
        return "0"
    
    answer = ''
    sort_n = sorted(list(map(str, numbers)), key = lambda x:x[0], reverse = True)
    
    same = 0
    for i in range(len(sort_n)-1):
        if (sort_n[i] == '0') or ( same == 0 and sort_n[i][0] != sort_n[i+1][0] ) :
            answer += sort_n[i]
        elif  sort_n[i][0] == sort_n[i+1][0] :
            same += 1
        else :   # same != 0 and sort_n[i][0] != sort_n[i+1][0] 
            answer += find_max(sort_n[i-same:i+1])
            same = 0
    
    answer += find_max(sort_n[-same-1:]) if same else sort_n[-1]
    return answer


# TEST CASE Ⅰ
numbers = [6, 10, 2]
print(solution(numbers))

# TEST CASE Ⅱ   
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

# TEST CASE Ⅲ
numbers = [0, 0, 0]
print(solution(numbers))

# TEST CASE Ⅳ
numbers = [1, 2, 21, 21]
print(solution(numbers))




### 두 번째 풀이 - permutations() 사용하지 않고 풀이
def find_max(num_list):
    len_c = [[],[],[],[]]    # 길이별로 분류하기 위한 list
    for n in num_list:   # 길이별로 분류하여 list에 저장
        len_c[len(n)-1].append(n)
        
    sort_nums = sum( [sorted(n, reverse=True) for n in len_c], [] )
    return ''.join(sort_nums)
    
def solution(numbers):
    if sum(numbers) == 0 :
        return "0"
    
    answer = ''
    sort_n = sorted(list(map(str, numbers)), key = lambda x:x[0], reverse = True)
    
    same = 0
    for i in range(len(sort_n)-1):
        if (sort_n[i] == '0') or ( same == 0 and sort_n[i][0] != sort_n[i+1][0] ) :
            answer += sort_n[i]
        elif  sort_n[i][0] == sort_n[i+1][0] :
            same += 1
        else :   # same != 0 and sort_n[i][0] != sort_n[i+1][0] 
            answer += find_max(sort_n[i-same:i+1])
            same = 0
    
    answer += find_max(sort_n[-same-1:]) if same else sort_n[-1]
    return answer



### 세 번째 풀이 - permutations() 사용하지 않고 풀이
def solution(numbers):
    if sum(numbers) == 0 :
        return "0"
    
    str_n = list(map(str, numbers))
    
    len_c = [[],[],[],[]]    # 길이별로 분류하기 위한 list
    for n in str_n:   # 길이별로 분류하여 list에 저장
        len_c[len(n)-1].append(n)
    
    sort_nums = sum( [sorted(n, reverse=True) for n in len_c], [] )
    
    return ''.join(sort_nums)
