def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    if not n % 4 == 0:
        print("NO")
        return
    result = list(range(2, n + 1, 2)) + list(range(1, n, 2))
    result[-1] += n // 2
    print("YES")
    print(*result)

t = int(input())
for i in range(t):
    solve()