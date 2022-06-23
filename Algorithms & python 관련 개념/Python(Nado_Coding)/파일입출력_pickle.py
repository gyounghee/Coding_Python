# pickle
# : 프로그램 상에서 사용하고 있는 data를 file 형태로 저장해주는 것
# - file을 누군가에게 주면 그 file을 열어서 pickle을 이용하거나 data를 가져와서 code를 또 쓸 수 있음

import pickle

# # 파일 쓰기
# # pickle을 쓰기 위해서는 항상 b(binary type)을 정의해줘야 하며, 따로 encoding을 정의해주지 않아도 됨 
# profile_file = open("profile.pickle", "wb")  
# profile = {"이름":"박명수", "나이":30, "취미":["수영","골프","코딩"]}
# print(profile)
# # pickle을 이용해서 data를 file에 쓰기위해
# # pickle.dump(data, file명)
# pickle.dump(profile, profile_file)     # profile에 있는 정보를 file에 저장
# profile_file.close()


# # 파일 읽기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)   # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()