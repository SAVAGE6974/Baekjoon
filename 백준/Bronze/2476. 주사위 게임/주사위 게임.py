n = int(input())
money=0
temp=0
for i in range(n):
    a, b, c = map(int, input().split())

    if (a == b) and (b == c):
        # case 1
        curr_mny = 10000+a*1000
        # print(curr_mny)

    elif ((a == b) and (b != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)):
        # case 2
        # print(a, b, c)
        if (a == b):
            curr_mny = a * 100 + 1000
            # print(curr_mny)
        elif (b == c):
            curr_mny = c * 100 + 1000
            # print(curr_mny)
        else:
            curr_mny = c * 100 + 1000
            # print(curr_mny)
    else:
        # case 3
        if a > b:
            temp = a
        elif b > a:
            temp = b

        if temp > c:
            pass
        elif temp < c:
            temp = c
        curr_mny = temp * 100
        # print(curr_mny)

    if curr_mny > money:
        money = curr_mny

print(money)