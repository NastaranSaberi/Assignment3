array = []
n = int(input("How many members does your array have ?"))
result = True

for i in range(n):
    number_array = int(input("Please enter your array members :"))
    array.append(number_array)

for i in range(len(array)-1):
    if array[i] > array[i+1]:
        result = False
        
       

if result :
    print(array,"\n","Array is sorted from small to large.\U0001f600")
else :
    print(array,"\n","Array is not sorted from small to large.\U0001f925")
 


