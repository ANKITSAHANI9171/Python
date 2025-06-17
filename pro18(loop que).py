#search for  a number x in these tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)

x=36

i=0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at inx",i)
        break          #break is used to stop the loop
    else:
        print("finding")
    i=i+1