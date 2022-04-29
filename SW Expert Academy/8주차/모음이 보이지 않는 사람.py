for c in range(int(input())):
     word = input()
     word = word.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
     print(f"#{c+1} {word}")
