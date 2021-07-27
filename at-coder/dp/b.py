def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    h = RA()
    dp = [0] * n
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        start = max(0, i - k)
        dp[i] = abs(h[i] - h[start]) + dp[start]
        for j in range(start + 1, i):
            dp[i] = min(dp[i], abs(h[i] - h[j]) + dp[j])
    print(dp[n - 1])
solve()