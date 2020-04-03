from typing import List
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # n -> [3]
        removed = {}
        self.total = n * 2
        def remove(n, t):
            if not n in removed.keys():
                removed[n] = [False, False, False]
                removed[n][t] = True
                self.total -= 1
                return
            tc = 0
            fc = 0
            for i in range(3):
                if removed[n][i]: tc += 1
                else: fc += 1
            if removed[n][t] == False and tc == 2:
                self.total -= 1
            removed[n][t] = True
            
        for r in reservedSeats:
            a = r[0]
            b = r[1]
            if 2 <= b and b <= 5: 
                remove(a, 0)
            if 4 <= b and b <= 7:
                remove(a, 1)
            if 6 <= b and b <= 9:
                remove(a, 2)
        return self.total

    def __init__(self):
        self.total = 0

s = Solution()
print(s.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
print(s.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]))
print(s.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]))
