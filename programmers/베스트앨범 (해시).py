def choice(best_album, genre_d, play_d):
    tmp = []
    for i in genre_d[max(play_d)]:
        tmp.append(plays[i])
    for _ in range(2):
        tmp_max = tmp.index(max(tmp))
        plays_max = genre_d[max(play_d)][tmp_max]
        best_album.append(plays_max)
        tmp[tmp_max], plays[plays_max] = 0, 0
    play_d[max(play_d)] = 0
    return best_album

def solution(genres, plays):
    best_album = []
    
    genre_d = dict.fromkeys(genres, ())
    for i in range(len(genres)):
        genre_d[genres[i]] += (i,)

    play_d = dict.fromkeys(genres, 0)
    for i in range(len(plays)):
        play_d[genres[i]] += plays[i]

    while sum(play_d.values()):
        best_album = choice(best_album, genre_d, play_d)
        
    return best_album

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))       # [4, 1, 3, 0]

