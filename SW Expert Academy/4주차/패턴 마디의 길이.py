for c in range(int(input())):
    word = input()
    w = {}
    for i in word :
        try : w[f'{i}'] += 1
        except : w[f'{i}'] = 1
    s = len(word)//min(w.values())
    if word[:s] == word[s:s+s] : print(f'#{c+1} {s}')
    else : print(f'#{c+1} {s-1}')
    
