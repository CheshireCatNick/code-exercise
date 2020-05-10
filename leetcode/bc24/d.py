class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        ways = [0] * len(s)
        ways[0] = 1
        for i in range(1, len(s)):
            start = i
            while int(s[start:i + 1]) <= k:
                if 10 ** (i - start) > k:
                    break
                if start == 0:
                    ways[i] += 1
                    break
                if not s[start] == "0":
                    ways[i] += ways[start - 1]
                    ways[i] %= 1e9 + 7
                start -= 1
        return int(ways[len(s) - 1] % (1e9 + 7))


s = Solution()
print(s.numberOfArrays("1234567890", 90))