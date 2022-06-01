# 이진 탐색하기 - binary search
## bisect - 배열 이진 분할 알고리즘


# bisect.bisect 메소드를 모르는 경우
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))


# bisect.bisect 메소드 이용
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
