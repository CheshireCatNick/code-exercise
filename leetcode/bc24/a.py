class Solution:
    def minStartValue(self, nums) -> int:
        start = 0
        mini = 1
        for n in nums:
            start += n
            mini = min(mini, start)
        if mini <= 0:
            return -mini + 1
        else:
            return 1

s = Solution()
print(s.minStartValue([1, -2, -3]))
