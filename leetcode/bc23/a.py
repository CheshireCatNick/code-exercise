class Solution:
    def getDS(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s
    def countLargestGroup(self, n: int) -> int:
        state = {}
        for i in range(1, n + 1):
            s = self.getDS(i)
            if s in state: state[s] += 1
            else: state[s] = 1
        m = 0
        for k in state:
            m = state[k] if state[k] > m else m
        c = 0
        for k in state:
            if state[k] == m:
                c += 1
        return c

        
s = Solution()
print(s.countLargestGroup(13))
print(s.countLargestGroup(2))
print(s.countLargestGroup(15))
print(s.countLargestGroup(24))