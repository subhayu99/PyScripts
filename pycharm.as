def des(n):
    if n==0 or n==1:
        print(n, end=" ")
        return
    dews(int(n/2))
    des(n%2)
    num = int(input("enter any decimal number"))
    print("Binary converted number")
          des(num)