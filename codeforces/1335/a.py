def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    if n % 2 == 0:
        print(n // 2 - 1)
    else:
        print(n // 2)

t = int(input())
for i in range(t):
    solve()