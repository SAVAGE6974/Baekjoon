a = 0
b = 0
who = 'D'

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

for i in range(10):
    if list_a[i] < list_b[i]:       # B가 이김
        who = 'B'
        b += 3
    elif list_a[i] > list_b[i]:     # A가 이김
        who = 'A'
        a += 3
    elif list_a[i] == list_b[i]:    # 비김
        a += 1
        b += 1

if a>b:
    who = 'A'
elif a<b:
    who = 'B'

print(a, b)
print(who)