na = 1
for i in range(3):
    na = na*int(input())
list_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
na = str(na)
for i in range(len(na)):
    if na[i] == '0':
        list_a[0] += 1
    elif na[i] == '1':
        list_a[1] += 1
    elif na[i] == '2':
        list_a[2] += 1
    elif na[i] == '3':
        list_a[3] += 1
    elif na[i] == '4':
        list_a[4] += 1
    elif na[i] == '5':
        list_a[5] += 1
    elif na[i] == '6':
        list_a[6] += 1
    elif na[i] == '7':
        list_a[7] += 1
    elif na[i] == '8':
        list_a[8] += 1
    elif na[i] == '9':
        list_a[9] += 1
for i in range(len(list_a)):
    print(list_a[i])