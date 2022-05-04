def solution(phone_book):
    phone_book.sort()   # 오름차순 정렬
    for i in range(len(phone_book)-1) :
        head = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:head] :
            return False
    return True


# TEST CASE Ⅰ
phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

# TEST CASE Ⅰ
phone_book = ["123","456","789"]
print(solution(phone_book))

# TEST CASE Ⅰ
phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))



## 다른 풀이 - 해시 이용
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True
