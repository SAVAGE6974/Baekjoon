n = int(input())
list_a = [i+1 for i in range(n)]
na = 0; kill = []
for i in range(len(list_a)-1):
    kill.append(list_a[0])
    del list_a[0]
    na = list_a[0]
    del list_a[0]

    list_a.append(na)

for i in range(len(kill)):
    print(kill[i], end=' ')
print(list_a[0])
