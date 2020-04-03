class Solution:
    def gp(self, n):
        if n in self.cache.keys():
            return self.cache[n]
        if n % 2 == 0:
            ans = self.gp(n / 2) + 1
        elif n % 2 != 0:
            ans = self.gp(n * 3 + 1) + 1
        self.cache[n] = ans
        return ans

    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = list(range(lo, hi + 1))
        nums.sort(key=self.gp)
        return nums[k - 1]
        
    def __init__(self):
        self.cache = {}
        self.cache[1] = 1

s = Solution()
print(s.getKth(1, 1000, 777))