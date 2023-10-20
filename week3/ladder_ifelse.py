grade = int(input('Enter your grade: (0-100) '))

if grade < 0 or grade > 100:
    print('Invalid grade!')
else:
    if grade < 40:
        print('Fail')
    elif grade <= 60:
        print('Pass')
    elif grade <= 80:
        print('Merit')
    else:
        print('Distinction')

print('Done')