from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for n in arr:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        m = -1
        for n in count:
            if n == count[n]:
                m = n if n > m else m
        return m

s = Solution()
print(s.findLucky([2, 2, 3, 4]))
print(s.findLucky([1, 2, 2, 3, 3, 3]))
print(s.findLucky([2, 2, 2, 3, 3]))
print(s.findLucky([5]))
print(s.findLucky([7, 7, 7, 7, 7, 7, 7]))