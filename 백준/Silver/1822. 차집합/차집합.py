a, b=map(int, input().split())
a=set()
b=set()

a.update(map(int, input().split()))
b.update(map(int, input().split()))

result=list(a.difference(b))
print(len(result))
result.sort()
for i in result:
    print(i, end=' ')
