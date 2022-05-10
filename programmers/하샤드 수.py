def solution(x):
    n_total = sum(list(map(int, list(str(x)))))
    return True if x % n_total == 0 else False
