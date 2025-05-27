while True:
    sum = 1
    s = input()
    if int(s) == 0:
        break
    else:
        for i in range(len(s)):
            if s[i] == '0':
                sum += 5
            elif s[i] == '1':
                sum += 3
            else:
                sum += 4
        print(sum)