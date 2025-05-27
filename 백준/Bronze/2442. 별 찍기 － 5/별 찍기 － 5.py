s=int(input())

for i in range(s):
    for j in range(s-i-1):
        print(' ', end='')
    for n in range(i+1):
        print('*', end='')
    for n in range(i):
        print('*', end="")
    print()