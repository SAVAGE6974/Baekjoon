s=int(input())

for i in range(1, s+1):
    print(' '*(i-1)+'*'*(s-i+1), end="")
    for j in range(s-i):
        print('*', end='')
    print()