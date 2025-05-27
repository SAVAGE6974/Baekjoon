s=int(input())

for i in range(s):
    for j in range(s-i-1):
        print(' ', end='')
    for n in range(i+1):
        print('*', end='')
    for n in range(i):
        print('*', end="")
    print()
for i in range(1, s):
    print(' '*(i)+'*'*(s-i-1), end="")
    for j in range(s-i):
        print('*', end='')
    print()
