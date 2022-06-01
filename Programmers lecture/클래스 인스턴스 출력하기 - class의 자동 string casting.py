# 클래스 인스턴스 출력하기 - class의 자동 string casting

## 다른 언어에서는 클래스 바깥에 출력 함수를 만들거나, print문 안에서 format을 지정
class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

point = Coord(1, 2)
print( '({}, {})'.format(point.x, point.y) ) 

# 또는
def print_coord(coord):
    print( '({}, {})'.format(coord.x, coord.y) )
print_coord(point)




## python은 __str__ 메소드를 이용해 class 내부에서 출력 format을 지정
