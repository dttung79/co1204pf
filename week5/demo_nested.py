answer = 'y'
while answer == 'y':
    n = int(input('Enter n: '))

    for i in range(1, 11):
        print(f'{i:2} x{n:2} = {n * i:2}')
    
    answer = input('Do you want to continue? (y/n) ')