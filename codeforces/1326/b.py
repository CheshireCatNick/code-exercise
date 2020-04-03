n = int(input())
b = input().split()
b = list(map(lambda x: int(x), b))
a = []
maxTilNow = 0
for i in b:
    j = i + maxTilNow
    a.append(j)
    maxTilNow = j if j > maxTilNow else maxTilNow

print(*a)