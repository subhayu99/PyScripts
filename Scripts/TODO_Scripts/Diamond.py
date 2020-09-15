''' Diamond Pattern
         *
        ***
       *****
        ***
         *
'''
    
def Diamond(rows): 
    n = 0

#---------------------------Upper Half--------------------------------
    
    for i in range(1, rows + 1):            # loop to print spaces 
        for j in range (1, (rows - i) + 1): 
            print(end = " ")
            
        while n != (2 * i - 1):             # loop to print star 
            print("*", end = "") 
            n = n + 1
        n = 0
        print()  
#---------------------------------------------------------------------

#---------------------------Lower Half--------------------------------
    k = 1
    n = 1
    for i in range(1, rows):                # loop to print spaces 
        for j in range (1, k + 1): 
            print(end = " ") 
        k = k + 1 
        while n <= (2 * (rows - i) - 1):    # loop to print star
            print("*", end = "") 
            n = n + 1
        n = 1
        print() 
#----------------------------------------------------------------------

rows=int(input("Enter no. of rows: "))
while (rows%2==0):
    print("Please enter ODD number of rows")
    rows=int(input("Enter no. of rows: "))
Diamond(rows)
