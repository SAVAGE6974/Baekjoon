n = int(input())
list_a = list(map(int, input().split()))
list_b = list()
m = max(list_a)
sum1 = 0
for i in list_a:
    list_b.append(i / m * 100)
for i in list_b: sum1 += i
print(sum1 / len(list_b))