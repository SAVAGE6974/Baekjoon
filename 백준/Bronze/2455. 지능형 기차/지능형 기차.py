m = 0
na = 0
for i in range(4):
    a, b = map(int, input().split(' '))
    m = m-a+b
    if na<m:
        na=m
print(na)