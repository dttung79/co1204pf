# Write a program that asks for a number n, then print 2 upside down triangles
# of asteriks.
# Example: n = 3
# Output:
# 1st triangle
# * * * * * 
#   * * *
#     *

n = int(input('Enter n: '))
for i in range(n):
    # draw i spaces
    for _ in range(i):
        print(' ', end=' ')
    # draw 2(n-i) - 1 asteriks
    for _ in range(2*(n-i)-1):
        print('*', end=' ')
    print()

# 2nd triangle
# * * *
#   * *
#     *

for i in range(n):
    # draw i spaces
    for _ in range(i):
        print(' ', end=' ')
    # draw 2(n-i) - 1 asteriks
    for _ in range(n-i):
        print('*', end=' ')
    print()
