list_a=[0 for i in range(100)]
s=int(input())
list_b=list(map(int, input().split()))
count=0
# print(list_b)
for i in list_b:
    if list_a[i-1]==1:
        count+=1
    else:
        list_a[i-1]=1
print(count)