n = int(input('Enter an even number: '))

while n % 2 != 0:
    n = int(input('Invalid number. Please try again: '))

print('Here is an even number', n)