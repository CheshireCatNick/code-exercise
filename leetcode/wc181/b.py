import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # return -1 if #div != 4
        # rerurn sum if #div == 4
        def getSum(n):
            target = math.floor(math.sqrt(n))
            s = 1 + n
            count = 2
            for i in range(2, target + 1):
                if n % i == 0:
                    if n / i == i:
                        count += 1
                        s += i
                    else:
                        count += 2
                        s += i + int(n / i)
                if count > 4:
                    return -1
            if count < 4:
                return -1
            return s
        r = 0
        for n in nums:
            s = getSum(n)
            if s != -1:
                r += s
        return r

s = Solution()
print(s.sumFourDivisors([21, 4, 7]))