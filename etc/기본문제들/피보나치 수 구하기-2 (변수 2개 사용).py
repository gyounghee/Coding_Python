def Fibonacci(f,s):
    first, second = s, f+s
    return first, second

num = int(input())  # 몇 번째 피보나치 수를 구할 것인지

for i in range(num+1): 
    if i == 0 :     # 0 번째면 first에 0 저장
        first = 0
    elif i == 1 :   # 1 번째면 second에 1 저장
        second = 1
    else :          # 두번쨰 부터는 first에 second값을 넣고 second에는 바로 앞 두 피보나치 수의 합을 넣는다
        first, second = Fibonacci(first,second)
print(second)
