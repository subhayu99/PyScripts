# Program to find the greatest number jn a list
arr=[1,2,3,4,5]

max=arr[0]
#comparing the max variable with rest of the array
for i in range(0,len(arr)):
    if arr[i]>max: 
       max=arr[i]

print(max)
