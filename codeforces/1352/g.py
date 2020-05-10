def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    if n < 4:
        print(-1)
        return
    ans = []
    if n % 2 == 0:
        s = n - 1
        while s >= 1:
            ans.append(s)
            s -= 2
        ans.append(4)
        ans.append(2)
        s = 6
        while s <= n + 1:
            ans.append(s)
            s += 2
    else:
        s = n
        while s >= 1:
            ans.append(s)
            s -= 2
        ans.append(4)
        ans.append(2)
        s = 6
        while s <= n - 1:
            ans.append(s)
            s += 2
    print(*ans)

t = int(input())
for i in range(t):
    solve()