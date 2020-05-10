def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    arr = RA()
    maxToNow = arr[0]
    maxFill = 0
    for i in range(1, n):
        maxToNow = max(maxToNow, arr[i])
        fill = maxToNow - arr[i]
        maxFill = max(maxFill, fill)
    ans = 0
    while maxFill > 0:
        ans += 1
        maxFill >>= 1
    print(ans)

t = int(input())
for i in range(t):
    solve()