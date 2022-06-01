# 2차원 list를 1차원 list로 만들기 - from_iterable

def solution(mylist):
    return sum(mylist, [])



## python을 사용하여 리스트 이어붙이기
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))


### 제한적으로 사용 가능한 방법 - Numpy 라이브러리의 flatten
#### - 각 원소의 길이가 동일한 경우에만 사용 가능
# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
