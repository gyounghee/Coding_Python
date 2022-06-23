# # pickle과 with 함께 이용
# import pickle

# # pickle을 통해 profile이라는 파일을 열고, profile_file이라는 변수로 저장
# with open("profile.pickle", "rb") as profile_file :  
#     # pickle.load(변수)를 통해서 file에 있는 정보를 읽음
#     print(pickle.load(profile_file))    

# # 따로 종료해줄 필요 없음
# # with를 빠져나오면서 자동 종료


# 일반적인 file의 읽고 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file :
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file :
#     print(study_file.read())
