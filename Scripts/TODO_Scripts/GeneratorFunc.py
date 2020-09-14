# A Python generator is a function which returns a generator iterator (just an object we can iterate over) by calling yield

def simpleGenerator(numbers):
    i = 0
    while True:
        check = input('Wanna generate a number? (If yes, press y else n): ')
        if check in ('Y', 'y') and len(numbers) > i:
            yield numbers[i]                 # TODO: Create a function of your own that does the same work as the "yield" function. You can use any other inbuilt function except the "yield" function.
            i += 1
        else:
            print('Bye!')
            break

for number in simpleGenerator([10, 11, 12, 14]):
    print(number)
