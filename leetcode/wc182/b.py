from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = {}
        for i in range(n):
            r = rating[i]
            count[r] = [0, 0]
            for j in range(i + 1, n):
                if rating[j] > r:
                    count[r][0] += 1
            for j in range(i + 1, n):
                if rating[j] < r:
                    count[r][1] += 1
        result = 0
        for i in range(n):
            r = rating[i]
            for j in range(i + 1, n):
                if rating[j] > r:
                    result += count[rating[j]][0]
                if rating[j] < r:
                    result += count[rating[j]][1]
        return result

s = Solution()
print(s.numTeams([2, 5, 3, 4, 1]))
print(s.numTeams([2, 1, 3]))
print(s.numTeams([1, 2, 3, 4]))