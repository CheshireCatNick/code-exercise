def longestCommonSuffix(a, b):
    la = len(a)
    lb = len(b)
    dp = [[0] * (lb + 1) for i in range(la + 1)]
    print(dp)
    dp[0][0] = 0
    dp[0][1] = 0
    dp[1][0] = 0
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else 0
    return dp

def longestCommonSubStr(a, b):
    lcs = longestCommonSuffix(a, b)
    print(lcs)
    bestI = -1
    bestJ = -1
    best = -1
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if lcs[i][j] > best:
                best = lcs[i][j]
                bestI = i
                bestJ = j
    return a[bestI - best:bestI]

print(longestCommonSubStr("aabbcv", "ddbcvv"))