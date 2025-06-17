#Recursion function

def show(n):
    if(n==0):         #base case
        return
    print(n)
    show(n-1)


show(5)    


#write a program to find the factorial using recursion 

def fact(n):
    if(n== 1 or n==0 ):
        return 1
    return fact(n-1) * n


print(fact(4))