#write a program to find the factorial of number given by user 
#using while loop
num=int(input("Enter Number: "))

fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print(fact)