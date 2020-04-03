
n = int(input())
digits = input()
dp = []
for i in range(n):
    dp.append([-1] * n)
for i in range(n):
    dp[0][i] = int(digits[i])
for i in range(1, n):
    for j in range(n - i):
        dp[i][j] = abs(dp[i - 1][j] - dp[i - 1][j + 1])
print(dp[n - 1][0])