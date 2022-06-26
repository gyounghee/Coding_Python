# 7568번 - 덩치

from sys import *
input = stdin.readline

N = int(input())
student = [ list(map(int, input().split())) for i in range(N) ]
student = [ [i] + v for i, v in enumerate(student) ]
student.sort(key = lambda x : (x[1], x[2]), reverse=True)

student[0] = [student[0][0], student[0][1], student[0][2], 1]
for i in range(1,N) :
    tmp = i+1
    for j in range(i-1,-1,-1) :
        if student[i][1] == student[j][1] or student[i][2] >= student[j][2] :
            tmp -= 1
    student[i] = [student[i][0], student[i][1], student[i][2], tmp]

seq = sum(sorted(student, key=lambda x : x[0]), [])
print( ' '.join(list(map(str, seq[3::4]))) )
