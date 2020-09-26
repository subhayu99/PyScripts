# Python program for a simple calculator 
import math
# Function to Add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to Subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 

# Function to Multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to Divide two numbers 
def divide(num1, num2): 
    return num1 / num2   

print("Please select operation -\n"\
        "1. Add\n"\
        "2. Subtract\n"\
        "3. Multiply\n"\
        "4. Divide\n"\
        "5. sin\n"\
        "6. cos\n"\
        "7. tan\n")\

# Take input from the user  
select = int(input("Select operation among 1, 2, 3, 4, 5, 6, 7: ")) 
  
number_1 = int(input("Enter first number: ")) 

number_2 = int(input("Enter second number: ")) 
 

if select == 1: 
    print("\n", number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2: 
    print("\n", number_1, "-", number_2, "=", subtract(number_1, number_2)) 

elif select == 3: 
    print("\n", number_1, "*", number_2, "=", multiply(number_1, number_2)) 

elif select == 4: 
    print("\n", number_1, "/", number_2, "=", divide(number_1, number_2))

elif select == 5:
    ch=int(input("Choose the number: "))
    if (ch==1):
        print("\nSin of ", number_1, "=", math.sin(number_1))
    else:
        print("\nSin of ", number_2, "=", math.sin(number_2))

elif select == 6:
    ch=int(input("Choose the number: "))
    if (ch==1):
        print("\nCos of ", number_1, "=", math.cos(number_1))
    else:
        print("\nCos of ", number_2, "=", math.cos(number_2))

elif select == 7:
    ch=int(input("Choose the number: "))
    if (ch==1):
        print("\nTan of ", number_1,"=", math.tan(number_1))
    else:
        print("\nTan of ", number_2,"=", math.tan(number_2))

else: 
    print("\nInvalid input")
