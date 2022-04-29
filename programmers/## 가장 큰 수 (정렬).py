# 아 몰라 일단 보 ;;;
def n_sort(n):
    tmp_1,tmp_2 = [],[]
    for i in range(len(n)):
        if len(n[i]) == 1 : tmp_1.append(n[i])
        else : tmp_2.append(n[i])
    n = sorted(tmp_2, key = lambda x : str(x)[1], reverse=True)
    for i in range(len(n)):
        if n[i][-1] == '0' : n[:-i] += tmp_1.pop(0)
    return n

def solution(numbers):
    answer = ""
    n = sorted(numbers, key = lambda x : str(x)[0], reverse=True)
    n, c =list(map(str, n)), 0
    
    for i in range(len(n)-1):
        if n[i][0] == n[i+1][0] : 
            c += 1
            if i == len(n)-2 and n[i] != '0':
                n[i-c+1:i+2] = n_sort(n[i-c+1:i+2])
        elif c > 0 and n[i][0] != n[i+1][0] :
            n[i-c:i+1] = n_sort(n[i-c:i+1])
            c = 0
    for i in n:
        answer += str(i)
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
numbers = [1, 10, 100, 1000]
print(solution(numbers))



