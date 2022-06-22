# 함수를 이런식으로 만들 경우 lang 변수들의 개수가 달라지거나 하면 함수 또는 매개변수를 변경해야 하는 불편함이 생김
# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print(f"이름 : {name}\t나이 : {age}\t", end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


## 이럴 때 사용하는 것이 "가변인자"
def profile(name, age, *language) :
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "JavaScript" ,"C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")