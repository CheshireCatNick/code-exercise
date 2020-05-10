def add1(arr):
    r = [0] * len(arr)
    carry = 1
    for i in range(len(arr) - 1, -1, -1):
        r[i] = carry + arr[i]
        if r[i] == 2:
            r[i] = 0
            carry = 1
        else:
            carry = 0
    if carry == 1:
        r = [1] + r
    return r
    
def d2(arr):
    arr.pop()
    
class Solution:
    def numSteps(self, s: str) -> int:
        arr = []
        for c in s:
            arr.append(int(c))
        count = 0
        l = len(arr)
        while l > 1:
            if arr[l - 1] == 0:
                d2(arr)
            else:
                arr = add1(arr)
            count += 1
            l = len(arr)
        return count

s = Solution()
print(s.numSteps("1101"))
print(s.numSteps("10"))
print(s.numSteps("1"))