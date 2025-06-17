#Find second largest number is an array
arr=list(map(int,input("Enter input:").split()))
def getsecondlargest(arr):
    n=len(arr)
    arr.sort()
    for i in range(n -2,-1,-1):
        if arr[i]!=arr[n-1]:
            return arr[i]
        return -1
print(getsecondlargest(arr))