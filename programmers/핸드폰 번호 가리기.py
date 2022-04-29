def solution(phone_number):
    answer = '*' * len(phone_number[:-4])+ phone_number[-4:]
    return answer

# TEST CASE Ⅰ
phone_number = "01033334444"
print(solution(phone_number))   # "*******4444"

# TEST CASE Ⅱ
phone_number = "027778888"
print(solution(phone_number))   # "*****8888"
