h, m = map(int, input().split(' '))
plus = int(input())
m += plus
while m >= 60:
    h += 1
    m -= 60

while h >= 24:
    h -= 24

print(h, m)