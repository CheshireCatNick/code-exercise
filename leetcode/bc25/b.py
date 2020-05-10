class Solution:
    def toList(self, n):
        s = str(n)
        return map(int, s.split())

    def maxDiff(self, num: int) -> int:
        num = str(num)
        a = ""
        for digit in num:
            if digit != "9":
                a = num.replace(digit, "9")
                break
        if a == "":
            a = num
        a = int(a)

        b = ""
        if num[0] != "1":
            # change to 1
            b = num.replace(num[0], "1")
        else:
            # first is 1
            # change first none 0 to 0
            for i in range(1, len(num)):
                if num[i] != "0" and num[i] != "1":
                    b = num.replace(num[i], "0")
                    break
        if b == "":
            b = num
        b = int(b)
        return a - b

s = Solution()
print(s.maxDiff(1101057))
# 9909000


