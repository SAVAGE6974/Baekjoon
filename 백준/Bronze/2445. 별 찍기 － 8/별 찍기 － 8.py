s=int(input())

for i in range(s):
    for j in range(i+1):
        print('*', end='')
    for j in range(2 * s - 2 - 2 * i):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(s - 1):

    for j in range(s - 1 - i):
        print('*', end='')
    for j in range(2 * (i + 1)):
        print(' ', end='')
    for j in range(s - 1 - i):
        print('*', end='')
    print()

#에휴...