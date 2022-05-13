# '수 정렬하기'는 Heap을 사용하여 문제해결
# '수 정렬하기'와 같은 방법으로 풀었을 때는 시간초과가 남
# sol 1 → sort, Heap등 이용 : 시간초과
# sol 2 → test case를 입출력(I/O)속도로 인해 시간초과가 남을 깨달음
#       → sys 모듈을 이용하여 sys.stdin.readline()으로 입력받는 방법으로 해결

# sys 모듈이란?
#  - 인터프리터에 의해 사용되거나 유지되는 일부 변수와 인터프리터와 강하게 상호작용하는 함수에 대한 엑세스를 제공
#  - sys 모듈은 python interpreter가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

# sys모듈에서 stdin이란?
#  - stdin은 모든 대화식 입력에 사용된다. ( input() 호출 포함 )
#  - 대화식 입력에 사용된다는 의미는 키보드로 입력하는 행위 뿐만 아니라 파일 등의 넓은 범위의 입력을 의미한다.

# stdin.readline()과 input()함수의 속도 차이
#  1. 두 함수간의 속도 차이는 Prompt 출력 여부와
#  2. 한번에 읽어와 버퍼에 저장하는 stdin.redline() 함수가 하나씩 누를 때마다 버퍼에 보관하는 input()보다 처리 속도가 빠르다.
#    → 즉, 버퍼 사이즈 차이로 입력이 반복될수록 stdin.readline()이 우위를 가진다.
#  3. input()함수의 경우 prompt message를 출력하고 개행 문자(\n)를 삭제한 값을 리턴하기 때문에 느린 것

from sys import stdin

n = int(stdin.readline())  # 줄 수
numbers = [int(stdin.readline()) for _ in range(n)]
numbers.sort()

for i in numbers:
    print(i)
