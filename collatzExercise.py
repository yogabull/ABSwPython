# This program explores the Collatz sequence.
'''
It is a function that passes a number,
If it is even, it should produce 'numberr // 2' and return that value.
If it is odd, collatz() should print and return 3 * number +1.
It should keep calling the new number until it returns an even number.
'''

def title():
    print('_____________________________')
    print('______ Collatz Sequence _____')
    print('_____________________________')


def intro():# This asks for user to input a number.
    number = input('Please enter a number: ')
    return number


def collatz_func(number): #This performs the collatz operations.
    print(number)
    while number % 2 !=0:
        number = number * 3 +1
        print(number)
    print('The final number is {}.'.format(number))


def main():
    title()
    number = intro()
    collatz_func(int(number))


main()
