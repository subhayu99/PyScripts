from random import choice
def yield_number(arr):
    check='y'
    while (check!='N' or check!='n'):
        check = input('Wanna generate a number? (If yes, press y else n): ')
        if (check=='Y' or check=='y'):
            print(choice(arr))
        else:
            print("Bye")
            break;

arr=[10, 11, 12, 14]
yield_number(arr)
