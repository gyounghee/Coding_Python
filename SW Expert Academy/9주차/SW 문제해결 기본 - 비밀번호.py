def check(password):
    if password[-1] == password[-2] :
        password.pop(-1)
        password.pop(-1)
    return password
    
for tc in range(10):
    str_len, p_str = input().split()
    p_str = list(p_str)
    password = []

    for p in range(int(str_len)):
        password.append(p_str.pop(0))
        if len(password) > 1 :
            check(password)
    
    print(f"#{tc+1} {''.join(password)}")
