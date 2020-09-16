'''Number1 * Number2 = L.C.M. * G.C.D. '''

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The L.C.M. of {} and {} is".format(num1,num2), compute_lcm(num1, num2))
