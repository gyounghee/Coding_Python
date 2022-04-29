num = int(input())  # 몇 번째 피보나치 수를 구할 것인지
li = []

for i in range(num+1): 
    if len(li) < 2 :  # li에 2개의 원소가 채워질 때까지는 그냥 채움
        li.append(i)
    else :   # li에 두개의 원소가 채워지면
        li.append(sum(li))   # li에 들어있 원소를 더하고 그 값을 li에 추가하기
        del li[0]  # li에 들어있는 첫 번째 원소 삭제하여 li에 두개의 원소만 존재하도록 함
print(li[1])
