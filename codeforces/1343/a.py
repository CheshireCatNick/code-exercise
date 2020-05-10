def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    s = 1
    p = 2
    while True:
        s += p
        if n % s == 0:
            print(n // s)
            return
        p *= 2

t = int(input())
for i in range(t):
    solve()