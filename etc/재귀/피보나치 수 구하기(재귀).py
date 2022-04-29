def Fibonacci(n):
    if n <= 0 : return 0
    elif n == 1 : return 1
    else : return Fibonacci(n-2)+Fibonacci(n-1)

n = int(input())
print(Fibonacci(n))
