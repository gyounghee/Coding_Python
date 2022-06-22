def std_weight(gender, height) :
    if gender == "남자" :
        return round(height * height * 22,2)
    elif gender == "여자" :
        return round(height * height * 21, 2) 

gender, height = "남자", 175  # 키는 cm 단위
print(f'키 {height}cm {gender}의 표준 체중은 {std_weight(gender, height/100)}kg 입니다.')