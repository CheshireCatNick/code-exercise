from typing import List

class Solution:
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [-1] * (amount + 1)
        self.dp[0] = 0
        for a in range(1, amount + 1):
            minimum = -1
            for coin in coins:
                rest = a - coin
                if rest < 0 or self.dp[rest] == -1:
                    continue
                use = self.dp[rest] + 1
                minimum = use if (use < minimum or minimum == -1) else minimum
            self.dp[a] = minimum
        return self.dp[amount]

    def __init__(self):
        # amount => minimum coins
        self.dp = []

s = Solution()
print(s.coinChange([2], 3))
# -1
s = Solution()
print(s.coinChange([1, 2, 5], 11))
# 3
s = Solution()
print(s.coinChange([186, 419, 83, 408], 6249))
# 20
s = Solution()
print(s.coinChange([388, 232, 419, 338, 49, 434, 4, 143], 4993))
# 13