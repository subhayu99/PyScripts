 # Python program for a simple calculator 
  
# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
	
# Function to find Sin of a number
def sinnum(num1):
    return math.sin(num1)

# Function to find Cos of a number
def cosnum(num1):
    return math.cos(num1)

# Function to find Tan of a number
def tannum(num1):
    return math.tan(num1)

#Function to take one input 
def one_input():
    num = int(input("Enter first number: "))
    return num

#Function to take two input 
def two_input():
    num_1 = int(input("Enter first number: ")) 
    num_2 = int(input("Enter second number: "))
    return num_1,num_2

print("Please select operation -\n"\
        "1. Add\n"\
        "2. Subtract\n"\
        "3. Multiply\n"\
        "4. Divide\n"\
        "5. Sin\n"\
        "6. Cos\n"\
        "7. Tan\n")

# Take input from the user  
select = int(input("Select operation among 1, 2, 3, 4, 5, 6, 7: ")) 
  
if select == 1: 
    number_1,number_2=two_input()
    print("\n", number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2: 
    number_1,number_2=two_input()
    print("\n", number_1, "-", number_2, "=", subtract(number_1, number_2)) 

elif select == 3: 
    number_1,number_2=two_input()
    print("\n", number_1, "*", number_2, "=", multiply(number_1, number_2)) 

elif select == 4: 
    number_1,number_2=two_input()
    print("\n", number_1, "/", number_2, "=", divide(number_1, number_2))

 elif select == 5:
    number_1=one_input  ()
    print("\nSin of ", number_1,"=",sinnum(number_1))

 elif select == 6:
    number_1=one_input()  
    print("\nCos of ", number_1,"=",cosnum(number_1))

 elif select == 7:
    number_1=one_input()  
    print("\nTan of ", number_1,"=",tannum(number_1))

else: 
    print("\nInvalid input")
