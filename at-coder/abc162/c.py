cache = {}
def gcd(a, b):
    if (a, b) in cache: 
        return cache[(a, b)]
    result = b if a % b == 0 else gcd(b, a % b)
    cache[(a, b)] = result
    cache[(b, a)] = result
    return result
def count(nums):
    freq = {}
    for n in nums:
        freq[n] = True
    if len(freq) == 1: return 1
    if len(freq) == 2: return 3
    return 6

k = int(input())
k += 1
s = 0
for i in range(1, k):
    for j in range(i, k):
        t = gcd(i, j)
        for l in range(j, k):
            s += gcd(t, l) * count([i, j, l])
print(s)
