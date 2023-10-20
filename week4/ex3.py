import random as rd

running = True
correct_guess = 0
incorrect_guess = 0

while running:
    comp_num = rd.randint(1, 5)
    user_num = int(input('Guess a number between 1 and 5: '))

    if comp_num == user_num:
        correct_guess += 1
        print('Correct')
    else:
        incorrect_guess += 1
        print('Incorrect')

    running = input('Do you want to continue? (y/n) ') == 'y'

print(f'Total correct guesses: {correct_guess}')
print(f'Total incorrect guesses: {incorrect_guess}')