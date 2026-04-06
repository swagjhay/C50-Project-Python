while True:
    try:
        n = int(input("Height: "))
        if 1 <= n <= 8:
            break
    except ValueError:
        pass

for i in range(n):
    #left pyramid space
    for j in range(n - i - 1):
        print(" ", end = "")
    #left bricks
    for j in range(i + 1):
        print("#", end = "")
    #Two spaces before each pyramid
    print("  ", end ="")

    #right bricks
    for j in range(i + 1):
        print("#", end = "")
    print()


