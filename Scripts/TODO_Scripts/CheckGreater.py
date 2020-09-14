#This prpgram checks that the given number is greater than all those numbers in th list

def checkGreater(number):
    '''This function checks whether the entered number is greater than those in the list'''
    original = [5,2,1,4,3]
    i,j=0,0
    for i in range (0,len(original)-1):             #Bubble Sort
        for j in range(0,len(original)-i-1):
            if original[j] > original[j+1] : 
                original[j], original[j+1] = original[j+1], original[j]
    print(original)
            
                                  
    if number > original[-1]:
        print('Yes, the entered number is greater than those in the list')
    else:
        print('No, entered number is less than those in the list')

if __name__ == '__main__':
    userInput = int(input('Enter the number to check: '))
    checkGreater(userInput)
