# Program to find the greatest number jn a list
arr=[1,2,3,4,5]

max=arr[0]
n=len(arr)

for i in range(n):
    if arr[i]>max: 
       max=arr[i]

print(max)
