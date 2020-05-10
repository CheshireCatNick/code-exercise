def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    arr = RA()
    if n == 1:
        print(0)
        return
    freq = {}
    for a in arr:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
    maxSame = 0
    for k in freq:
        maxSame = max(maxSame, freq[k])
    ans = min(maxSame, len(freq) - 1)
    ans2 = min(maxSame - 1, len(freq))
    print(max(ans, ans2))

t = int(input())
for i in range(t):
    solve()
