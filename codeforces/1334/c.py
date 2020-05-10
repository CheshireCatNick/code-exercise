def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    mons = []
    for i in range(n):
        mons.append(RA())
    groupD = 0
    minCost = mons[0][0]
    for i in range(n):
        prev = n - 1 if i == 0 else i - 1
        minCost = min(minCost, mons[i][0])
        if mons[prev][1] >= mons[i][0]:
            continue
        # i is a head
        groupD += mons[i][0] - mons[prev][1]
        minCost = min(minCost, mons[prev][1])
    print(groupD + minCost)

t = int(input())
while t > 0:
    solve()
    t -= 1