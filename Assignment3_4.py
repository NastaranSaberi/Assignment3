n = int(input("The length of the snake \n(Please enter a natural number) :"))

for i in range(n) :
    if i % 2 == 0:
        print("*",end="")

    else:
        print("#", end="")



