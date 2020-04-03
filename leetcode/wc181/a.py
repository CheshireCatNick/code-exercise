from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        i = 0
        for n in nums:
            result.insert(index[i], n)
            i += 1
        return result
            



s = Solution()
print(s.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))