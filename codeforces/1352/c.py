def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    rep = n - 1
    count = k // rep
    remainder = k % rep
    if remainder == 0:
        print(n * (count - 1) + rep)
    else:
        print(n * count + remainder)


t = int(input())
for i in range(t):
    solve()