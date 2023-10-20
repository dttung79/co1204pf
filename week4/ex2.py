counter = 0

while counter < 5:
    n = int(input('Enter an even number: '))
    if n % 2 == 0:
        counter += 1

print(f'Enough even numbers: {counter}')