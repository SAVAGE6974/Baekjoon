list_a=[]
a = 0
b = 0
for i in range(9):
    list_a.append(int(input()))
list_a.sort()

sum=sum(list_a)

for i in range(len(list_a)):
    for j in range(i+1, len(list_a)):
        if sum-list_a[i]-list_a[j]==100:
            a = i
            b = j

for k in range(len(list_a)):
    if k==a or k==b:
        continue
    else:
        print(list_a[k])