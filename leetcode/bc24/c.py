class Solution:
    def genHappyString(self, prefix, length):
        if length == 0:
            #print(prefix)
            self.k -= 1
            if self.k == 0:
                self.result = prefix
            return
        for c in self.alphas:
            if not len(prefix) == 0 and c == prefix[-1]:
                continue
            else:
                self.genHappyString(prefix + c, length - 1)

    def getHappyString(self, n: int, k: int) -> str:
        self.alphas = ['a', 'b', 'c']
        self.k = k
        self.count = 0
        self.result = ""
        self.genHappyString("", n)
        return self.result

s = Solution()
print(s.getHappyString(10, 100))