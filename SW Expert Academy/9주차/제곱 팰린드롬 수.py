# 앞으로 읽어도 뒤로 읽어도 똑같은 문자열 == 회문 == 팰린드롬
# 양의 정수 N에 대해 N과 루트N이 모두 팰린드롬이면  →  이 수를 제곱 팰린드롬 수   라고 함

for tc in range(int(input())):
    A, B = map(int, input().split())
    count = 0
    
    for i in range(A,B+1):
        num, num_r = i, i**(1/2)
        if num_r - int(num_r) == 0 :
            if str(num) == str(num)[::-1] and str(int(num_r)) == str(int(num_r))[::-1] :
                count += 1
    
    
    print(f"#{tc+1} {count}")
