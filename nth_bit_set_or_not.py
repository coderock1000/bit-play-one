def set(number, n):
    if number & (1 << (n - 1)):
        print('\n SET')
    else:
        print('\n not SET')

number = int(input('enter number: '))
n = int(input('enter bit number: '))
set(number, n)