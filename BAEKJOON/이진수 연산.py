# 12813번 - 이진수 연산

A = int(input(), 2)
B = int(input(), 2)

mask = 2 ** 100000 -1

print(bin(A&B)[2:].zfill(100000),
      bin(A|B)[2:].zfill(100000),
      bin(A^B)[2:].zfill(100000),
      bin(A ^ mask)[2:].zfill(100000),
      bin(B ^ mask)[2:].zfill(100000), sep='\n')
