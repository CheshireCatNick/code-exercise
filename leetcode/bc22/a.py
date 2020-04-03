from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr = []
        for n in arr1:
            arr.append((n, 1))
        for n in arr2:
            arr.append((n, 2))
        print(arr)
        arr.sort()
        print(arr)
        

s = Solution()
s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2)