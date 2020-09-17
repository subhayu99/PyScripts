def des(n):
       if (n>1):
         des(n//2)
    print(n%2,end=" ")
        print(n, end=" ")
        return
    des(int(n/2))
    des(n%2)
    num = int(input("Enter any decimal number"))
    print("Binary converted number")
          des(num)
