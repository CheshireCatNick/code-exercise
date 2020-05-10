class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = {}
        for c in s:
            if c in freq: freq[c] += 1
            else: freq[c] = 1
        sinCount = 0
        for c in freq:
            if freq[c] % 2 == 1:
                sinCount += 1
        sinCount = 1 if sinCount == 0 else sinCount
        return sinCount <= k and k <= len(s)

        
s = Solution()
print(s.canConstruct("annabelle", 2))
s.canConstruct("leetcode", 3)
s.canConstruct("true", 4)
s.canConstruct("yzyzyzyzyzyzyzy", 2)
s.canConstruct("kr", 7)
