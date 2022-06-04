# 2 x n 타일링

#### 풀이 1
# - 정확성, 효율성 통과
def solution(n):
    tile1, tile2 = 2, 3
    if n == 2 :    return 2
    elif n == 3 :  return 3
    else :
        for i in range(4,n+1):
            tile1, tile2 = tile2, tile1+tile2
        return tile2 % 1000000007

#### 풀이 2
# - 정확성은 통과 & 효율성 2/6통과
# - list에서 꺼내고 집어넣고 하는데 효율성이 조금 떨어지는 것 같음
def solution(n):
    tiles = [0,0,2,3]
    if n <= 3 :
        return tiles[n]
    else :
        for t in range(4,n+1):
            tiles.append(tiles[t-1]+tiles[t-2])
        return tiles[n] % 1000000007


