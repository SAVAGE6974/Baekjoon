a, b = map(int, input().split())
num = 1
list_a = []

for i in range(a):
    if a % num == 0:
        list_a.append(num)
        num += 1
    elif a % num > 0:
        num += 1

if len(list_a)<b or len(list_a)<0:
    print(0)
else:
    print(list_a[b-1])
#ㅅㅂ