# n = int(input('Enter a number: '))

# if n % 2 == 0:
#     print(f'{n} is even')
# else:
#     print(f'{n} is odd')

# Validation
# english = int(input('Enter English grade (0-10): '))
# if english < 0 or english > 10:
#     print('Invalid English grade')
# else:
#     print('English grade:', english)

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# m = a if a > b else b
# print('Max =', m)

name = input('Enter student name: ')
english = int(input('Enter English grade: '))
math = int(input('Enter Math grade: '))

if english < 0 or english > 10:
    print('Invalid English grade')
elif math < 0 or math > 10:
    print('Invalid Math grade')
else:
    if english > math:
        print(f'{name} should choose Business program')
    elif math > english:
        print(f'{name} should choose Computing program')
    else:
        print(f'{name} can choose either program (Business or Computing)')