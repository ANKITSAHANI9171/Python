#break and continue in loop


#example of break
i=1
while i<=5:
    if(i==3):
        break      #break is used to stop the loop
    print(i)
    i=i+1

print("end of break example")


#example of continue

i=1
while i<=5:
    if(i==3):         #skip
        i=i+1
        continue    #continue is used to terminate execution in current iteration & 
    print(i)           #continue execution of the
    i=i+1             # loop with the next iteration

print("end of continue example")