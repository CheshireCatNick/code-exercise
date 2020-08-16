import math
def RA():
    return list(map(int, input().split()))

def solve():
    n, m = input().split()
    n = int(n)
    m = int(float(m) * 100)
    print((n * m) // 100)


solve()