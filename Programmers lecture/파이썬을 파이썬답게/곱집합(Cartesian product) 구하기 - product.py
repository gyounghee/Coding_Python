# 곱집합(Cartesian product) 구하기 - product

# 이 함수를 모르는 경우
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)



# itertools.product를 이용
# itertools.product(*iterables, repeat=1)
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))


# * 공식문서
# - https://docs.python.org/3/library/itertools.html#itertools.product
