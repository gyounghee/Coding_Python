# 도전 1
def solution(n):
    answer = 0
    ary = [i for i in range(2,n+1)]
    num = [2,3,5,7]
    tmp = []
    for i in ary:
        if i in num or i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
            tmp.append(i)
    for i in range(len(tmp)):
        c = 0
        for j in range(1,tmp[i]+1):
            if c >= 3 : break
            elif tmp[i] % j == 0 : c += 1
        if c == 2 :
            answer += 1
    return answer


# 도전 2
def solution(n): 
    num_list = [i for i in range(2,n+1)]
    num_rm = []
    i = 2

    while i * i < n:
        j = 2
        while i*j <= n :
            if (i*j) in num_list :
                num_rm.append(i * j)
            j += 1
        i = num_list[num_list.index(i)+1]        
    return len(num_list)-len(list(set(num_rm)))


# 도전 3
def solution(n):
    answer = 0
    num_list = list(range(2,n+1))
    
    for i in range(2,n+1):
        rn = int( i ** (1/2) )
        tmp = [] # 루트를 씌운 수 이하의 소수를 담는 변수
        if rn == 1 :
            answer += 1
        else : # 루트를 씌운 수 이하의 소수를 찾기
            for j in range(2, rn+1): 
                c = 0
                for k in range(1,j+1):
                    if j % k == 0 : c += 1
                    if c > 2 : break
                if c == 2 : 
                    tmp.append(j)
            # 확인
            chk = 0
            for check in tmp:
                if i % check == 0 : chk += 1
            if chk == 0 : answer += 1
    
    return answer

n = 5
print(solution(n))


# -------------------------------------------------
# '에라토스테네스의 체' 이용

# 다른 사람 풀이 1

def solution(n):

    sieve = [True]*(n+1) # 0~n까지 칸을 True로 초기화

    m = int(n ** 0.5)  # 루트 n (제곱근 n)을 m 변수에 저장  -  어떤 자연수 n이 있을 때, √n 보다 작은 모든 소수들로 나누어 떨어지지 않으면 n은 소수
    for i in range(2, m+1): # 2부터 √n까지 
        if sieve[i] == True:  # 만약 해당 번호가 True면
            for j in range(i*i, n+1, i): # 해당 번호 * 2 부터 n까지 해당 번호의 배수를 False로 만듦
                sieve[j] = False

    x = [i for i in range(2, n+1) if sieve[i] == True]  # sieve 리스트 요소 중 2 번째 부터 True인 수만 찾아서 x 리스트 생성
    answer = len(x)    # answer은 x의 길
    return answer



# 다른 사람 풀이 2
def solution(n):
    num=set(range(2,n+1))   # 2~n까지의 수를 set타입으로 생성

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))  # i의 배수들을 num에서 지움
    return len(num)  



# +) python set타입
#   - 수학에서의 집합과 비슷
#   - 순서가 없고(인덱싱 불가) 중복이 없으며, mutable(변하기 쉬운) 객체이다
#   - 중괄호 { } 를 사용한다는 점에서 dictionary와 비슷하지만, key가 없다.

# ----------------------------------------------------------------

#   * 값 추가
#     - 변수명.add(추가할 값)
#     - 변수명.update([추가할 값1, 추가할 값2,..])
#   * 값 삭제
#     - 변수명.remove(삭제할 값)
#     - 변수명 -= {삭제할 값1, 삭제할 값2,...}

# ----------------------------------------------------------------

#   * 교집합
#     -  변수명 &  변수명
#     -  변수명.intersection( 변수명)
#   * 합집합
#     -  변수명 |  변수명
#     -  변수명.union( 변수명)

#   * 차집합
#     -  변수명 -  변수명
#     -  변수명.difference(변수명)
#   * 대칭자 (배타적 논리합) 집합
#     : x나 y 중 한 쪽에만 있는 요소들 즉, 대칭자는 중복되는 요소를 뺸 나머지 요소만 추출한다.
#     - (변수1-변수2)|(변수2-변수1)
