# 2720번 - 세탁소 사장 동혁
# Greedy를 이용한 문제 풀이 

for tc in range( int(input()) ) :
    change = int(input())
    QDNP = [25,10,5,1]

    for i in range(len(QDNP)) :
        QDNP[i], change = divmod(change, QDNP[i])

    print(QDNP[0],QDNP[1],QDNP[2],QDNP[3])
