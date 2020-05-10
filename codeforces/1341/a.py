def RA():
    return list(map(int, input().split()))

def solve():
    n, a, b, c, d = RA()
    pa = (a - b) * n
    pb = (a + b) * n
    sa = c - d
    sb = c + d
    if (sa <= pa and pa <= sb) or (sa <= pb and pb <= sb) or (pa <= sa and sb <= pb):
        print("Yes")
    else:
        print("No")

t = int(input())
for i in range(t):
    solve()