class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        i = 0
        while fib[-1] < k:
            fib.append(fib[i] + fib[i + 1])
            i += 1
        i = len(fib) - 1
        count = 0
        while True:
            if k == 0:
                break
            if fib[i] <= k:
                k -= fib[i]
                count += 1
            i -= 1
        return count
s = Solution()
print(s.findMinFibonacciNumbers(19))