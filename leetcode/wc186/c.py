class Solution:
    def findDiagonalOrder(self, nums):
        data = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                data.append((i + j, -i, nums[i][j]))
        data.sort()
        return [d[2] for d in data]
        
s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))