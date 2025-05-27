hap=0
low=999


for i in range(7):
    number=int(input())

    if(number % 2 == 1):
        hap += number

        if(low>number):
            low=number


if(hap==0):
    print(-1)
else:
    print(hap)
    print(low)