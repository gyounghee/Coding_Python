def Russian(left,right):
    global total
    if left % 2 == 1 :
        total += right
        if left == 1 : return
        else : Russian(left//2, right*2)
    else : Russian(left//2, right*2)

left, right = map(int, input().split())
total = 0
Russian(left,right)
print('왼쪽이 홀수인 오른쪽 수 들의 합은',total)
