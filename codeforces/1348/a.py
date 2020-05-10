def RA():
    return list(map(int, input().split()))

def s(n):
    return (1 << (n + 1)) - 2

def solve():
    n = int(input())
    print(2 * s(n//2 - 1) + 2)

t = int(input())
for i in range(t):
    solve()