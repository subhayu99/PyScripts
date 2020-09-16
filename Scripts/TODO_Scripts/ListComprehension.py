#This function is an implementation of how list comprehension works

n = int(input("Enter a number as a range: "))
print("A list of numbers of squares up to the given number is:")

'''print([x**2 for x in range(n)])'''  #Using List Comprehension
for i in range(1,n+1):
    if (i<n):
        print(i**2,end=', ')
    else:
        print(i**2)

print()
print("Converting the list of numbers till the given number to string data type:")

'''print([str(x) for x in range(n)])''' #Using List Comprehension
for i in range(0,n+1):
    if (i<n):
        print(str(i),end=', ')
    else:
        print(str(i))
