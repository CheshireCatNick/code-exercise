def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    move = 0
    ans = 0
    for i in range(1, n + 1, 2):
        ans += move * (i - 1) * 4
        move += 1
    print(ans)

t = int(input())
for i in range(t):
    solve()