n=input()
list_a=[0]*9
for i in n:
    na = int(i)
    if na==9:
        na=6
    list_a[na]+=1
list_a[6]=(list_a[6]+1)//2
print(max(list_a))