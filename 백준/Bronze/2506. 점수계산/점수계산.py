n=int(input())
scores=list(map(int, input().split(' ')))
tot=0
combo=0

for i in range(len(scores)):
    if scores[i]==0:
        combo=0
    else:
        tot += scores[i]+combo
        combo += 1


print(tot)