# A woman calculates payment for groceries for a week (7 days).
# For each day, she will enter the grocery name and price.
# The program will ask if she wants to continue other groceries.
# When finish for a day, the program will print the total price for that day 
# then moving on to the next day.
# Hints: using for loop for 7 days, using while loop for each day.
week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in range(7):
    print(f'Shoping for {week_days[day]}')
    total = 0
    shopping = True
    
    while shopping:
        name = input('Enter grocery name: ')
        price = int(input('Enter price: '))
        total += price
        shopping = input('Continue? (y/n) ') == 'y'
    
    print(f'Total for day {week_days[day]}: {total}')