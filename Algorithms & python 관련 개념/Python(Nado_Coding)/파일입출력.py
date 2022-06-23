# # 파일 생성 후 입력
# score_file = open("score.txt", "w", encoding="utf8")     # w : 쓰기용도
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# # 파일을 열었을떈 항상 닫아주는것도 해줘야함
# score_file.close()

# # 파일 내용 추가
# score_file = open("score.txt", "a", encoding="utf8")     # a : 이미 존재하는 파일에 이어서 쓰고싶을 때 
# # write를 통해서 적을 떄는 줄바꿈이 없음
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 80")
# score_file.close()

# # 파일 읽기 (전체 읽기)
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())    
# score_file.close()

# # 파일 읽기 (부분 읽기)
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")     # 한 줄을 읽고, 커서를 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# # 파일이 총 몇 줄 인지 모를 때 읽어오기
# # 방법 1 - while문 이용
# score_file = open("score.txt", "r", encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line : break
#     print(line, end="")
# score_file.close()

# # 방법2 - list에 값 넣은 후 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()    # 모든 라인을 가져온 후 list로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()