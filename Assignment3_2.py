import random

n = int(input("How many numbers do you want your array to have? "))
array = []
number = random.sample(range(0,n*n),n)
print("array:",number)



