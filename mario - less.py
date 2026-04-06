#Run till user enter value greater than 0
while True:
    try:
        n = int(input("height: "))
        if 1 <= n <= 8:
            break
    except ValueError:
        pass #do nothing and continue the loop
#Loop
for i in range(n):
    #print spaces before the bricks
    for j in range(n - i - 1):
        print(" ", end="")
    #print bricks for current row
    for j in range(i + 1):
        print("#", end ="")
    #move to next line
    print()
