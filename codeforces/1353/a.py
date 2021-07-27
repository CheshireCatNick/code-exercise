def RA():
    return list(map(int, input().split()))

def solve():
    n, m = RA()
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2 * m)

t = int(input())
for i in range(t):
    solve()