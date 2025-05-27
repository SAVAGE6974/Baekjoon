list_a=[]
for i in range(9):
    list_a.append(list(map(int, input().split())))
a = 0; x, y = 0, 0
for i in range(len(list_a)):
    for j in range(len(list_a[i])):
        if a < list_a[i][j]:
            a = list_a[i][j]
            x, y = i, j
print(a); print(x+1, y+1)