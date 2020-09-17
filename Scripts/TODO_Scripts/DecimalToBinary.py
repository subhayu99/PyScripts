def des(n):
    if(n > 1):
        des(n // 2)
    print(n %2, end='')
n=int(input("Enter the Decimal number: "))
print("Converted Decimal number: ",end='')
des(n)
