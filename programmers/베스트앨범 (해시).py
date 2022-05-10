def get_key(dict, v):
    return next(key for key, value in dict.items() if v == value)

def choice(plays, genre, genre_d, play_d):
    album, tmp = [], []
    for i in genre_d[genre]:
        tmp.append(plays[i])
    for _ in range(2):
        if sum(tmp) == 0 : break
        tmp_max = tmp.index(max(tmp))
        plays_max = genre_d[genre][tmp_max]
        album.append(plays_max)
        tmp[tmp_max], plays[plays_max] = 0, 0
    for g in genre_d[genre]:
        play_d[g] = 0
    return album

def solution(genres, plays):
    best_album = []

    play_d = {}
    for p in range(len(plays)):
        play_d[p] = plays[p]
        
    genre_d = dict.fromkeys(genres, ())
    for i in range(len(genres)):
        genre_d[genres[i]] += (i,)
    
    play_total = dict.fromkeys(genres, 0)
    for i in range(len(plays)):
        play_total[genres[i]] += plays[i]

    while sum(play_d.values()):
        genre = get_key(play_total, max(play_total.values()))
        best_album += choice(plays, genre, genre_d, play_d)
        play_total[genre] = 0
        
    return best_album

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))       # [4, 1, 3, 0]

genres = ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
plays = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(genres, plays))       # [0, 1, 2, 4]

genres = ["a", "b", "c", "d", "e", "f"]
plays = [1, 2, 3, 4, 5, 6]
print(solution(genres, plays))       # [5, 4, 3, 2, 1, 0]



## 다른 사람 풀이 1    -   공부 후 다시 분석 할 예정ㅠ 
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)  # ?
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]   # ?
        answer += temp[:min(len(temp),2)]
    return answer


## 다른 사람 풀이 2 - 코드 분석 완료
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:    #  dic1은 장르별 (고유번호, 플레이 횟수)에 대한 정보를 담는 dictionary
            dic1[g] = [(i, p)]  
        else:
            dic1[g].append((i, p))

        if g not in dic2:     # dic2는 장르별 플레이 횟수를 합산한 dictionary
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):     # 장르별 플레이 횟수에 대하여 내림차순으로 정렬 한 후 장르별로 살펴봄
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:  # 플레이 횟수에 대하여 내림차순으로 정렬 후 두 개를 슬라이싱 한 후 
            answer.append(i)                                                 # answer에 고유번호 추가 
    return answer
