class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        if n in self.dp.keys(): return self.dp[n]
        total = 0
        for r in range(1, n + 1):
            total += self.numTrees(r - 1) * self.numTrees(n - r)
        self.dp[n] = total
        return total
        
    def __init__(self):
        self.dp = {}

s = Solution()
print(s.numTrees(30))