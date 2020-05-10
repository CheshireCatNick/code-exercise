def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    a = RA()
    s = set(a)
    if k < len(s):
        print(-1)
        return
    rep = [1 for i in range(k - len(s))] + list(s)
    print(len(rep) * n)
    print(*rep * n)

t = int(input())
for i in range(t):
    solve()