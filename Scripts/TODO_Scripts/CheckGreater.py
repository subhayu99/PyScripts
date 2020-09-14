#This prpgram checks that the given number is greater than all those numbers in th list

def checkGreater(number):
    '''This function checks whether the entered number is greater than those in the list'''
    original = [1,2,3,4,5]
    original.sort()                              # TODO: Remove this inbuilt function (.sort) without changing the functionality of the program
    if number > original[-1]:
        print('Yes, the entered number is greater than those in the list')
    else:
        print('No, entered number is less than those in the list')

if __name__ == '__main__':
    userInput = int(input('Enter the number to check: '))
    checkGreater(userInput)
