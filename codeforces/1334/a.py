def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    records = []
    for i in range(n):
        records.append(RA())
    for r in records:
        if r[0] < r[1]:
            print("NO")
            return
    for i in range(1, n):
        if records[i][0] < records[i - 1][0] or records[i][1] < records[i - 1][1]:
            print("NO")
            return
        if records[i][0] - records[i - 1][0] < records[i][1] - records[i - 1][1]:
            print("NO")
            return
    print("YES")
    

t = int(input())
while t > 0:
    solve()
    t -= 1