def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    h = RA()
    dp = [0] * n
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        dp[i] = min(abs(h[i] - h[i - 1]) + dp[i - 1], abs(h[i] - h[i - 2]) + dp[i - 2])
    print(dp[n - 1])

solve()