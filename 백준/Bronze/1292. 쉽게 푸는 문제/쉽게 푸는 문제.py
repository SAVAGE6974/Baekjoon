a, b = map(int, input().split())
list_a=[]
sum = 0
for i in range(b):
    for j in range(i + 1):
        list_a.append(i + 1)
        if len(list_a) >= b:
            break
    if len(list_a) >= b:
        break
for i in range(a, b+1):
    sum += list_a[i - 1]
print(sum)