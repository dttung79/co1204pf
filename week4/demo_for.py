# print Hello World 10 times
for i in range(10):
    print('Hello World!')

# print numbers from 10 to 19
for i in range(10, 20):
    print(i, end=' ')

print()
# calculate sum of 50 numbers
s = 0
for i in range(1, 51):
    s += i

print(f'Sum from 1 to 50 = {s}')

# Calculate sum of even numbers from 1 to 100
s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s += i

print(f'Sum of even numbers from 1 to 100 = {s}')

s = 0
for i in range(2, 101, 2):
    s += i
print(f'Sum of even numbers from 1 to 100 = {s}')


for i in range(1, 101):
    print(f'{i:2}', end=' ')
    if i % 10 == 0:
        print()