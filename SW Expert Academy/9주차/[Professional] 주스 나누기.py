for tc in range(int(input())):
    Person = int(input())
    div = [f"1/{Person}" for _ in range(Person)]
    
    print(f"#{tc+1} {' '.join(div)}")
