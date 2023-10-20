n = 5

for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

n = int(input('Enter n: '))
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

print()

for i in range(n):
    for j in range(n - i):
        print('*', end=' ')
    print()

print()

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()




for i in range(n):
    # draw spaces
    for j in range(n - i - 1):
        print(' ', end=' ')
    # draw asterisks
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(2 * i + 1):
        print('*', end=' ')
    print()