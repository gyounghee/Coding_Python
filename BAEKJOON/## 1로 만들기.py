# 실패

num = int(input())
calc = 0

while num != 1 :
    if num % 3 != 0 :
        num -= 1
        calc += 1
    elif num % 3 == 0 :
        calc += int(num **(1/3))
        num //= 3 ** int(num **(1/3))
    elif num % 2 == 0 :
        calc += int(num **(1/2))
        num //= 2 ** int(num **(1/2))
    
print(calc)

