#write a program to find the factorial of n .(n is the parameter)

def calc_fact(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    print(fact)


calc_fact(5) 

calc_fact(6)



#write a program to convert USD to INR

def converter(usd_val):
    inr_val=usd_val * 83
    print(usd_val,"USD=", inr_val,"INR")


converter(4)

converter(2)