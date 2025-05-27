s=int(input())

for i in range(s):
    for j in range(s-i):
        print('*', end='')
    print()