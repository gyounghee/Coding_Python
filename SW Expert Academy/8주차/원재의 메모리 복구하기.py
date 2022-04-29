for c in range(int(input())):
    memory = list(input())
    initial_mem = ["0" for _ in range(len(memory))]
    count = 0
    for i in range(len(memory)):
        if memory[i] != initial_mem[i] : 
            initial_mem[i:] =  [f"{memory[i]}" for _ in range(len(memory) - i)]
            count += 1
    print(f"#{c+1} {count}")
