
#Find largest number is an array
array=[10,20,40,30]

if (array[0]>array[1] and array[0]>array[2] and array[0]>array[3]):
    print(array[0])
elif(array[1]>array[0] and array[1]>array[2] and array[1]>array[3]):
    print(array[1])
elif(array[2]>array[0] and array[2]>array[1] and array[2]>array[3]):
    print(array[2])
else:
    print(array[3])
