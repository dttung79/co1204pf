# Case 1: using counter with while loop
# counter = 0

# while counter < 10:
#     print('Hello world')
#     counter += 1

# Case 2: validating user input until it is correct
# n = int(input('Enter a positive number: '))

# while n <= 0:
#     n = int(input('Invalid number. Please try again: '))

# print('You entered', n)

# Case 3: asking user to stop or continue
running = True
s = 0
while running:
    n = int(input('Enter any number: '))
    s += n
    answer = input('Do you want to continue? (y/n) ')
    running = answer != 'n'

print(f'The sum of all numbers is {s}')