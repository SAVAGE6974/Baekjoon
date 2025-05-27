n, c = map(int, input().split())
lst = [0 for _ in range(c+1)]
cnt = -1

for _ in range(n):
    k = int(input())

    for i in range(0, c+1, k):
        if lst[i] == 0:
            cnt += 1
            lst[i] = 1

if cnt < 0:
    print(0)
else:
    print(cnt)