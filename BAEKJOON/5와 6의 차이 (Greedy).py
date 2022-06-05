# 2864번 - 5와 6의 차이
# Greedy를 이용한 문제 풀이

a, b = input().split()

a, b = a.replace('5','6'), b.replace('5','6')
sum_max = int(a) + int(b)
a, b = a.replace('6','5'), b.replace('6','5')
sum_min = int(a) + int(b)

print(sum_min, sum_max)


## 다른 풀이 분석
# eval() 함수를 이용한 풀이 
s=input()
def r(a,b): return eval(s.replace(a,b).replace(' ','+'))
print("{} {}".format(r('6','5'),r('5','6')))
