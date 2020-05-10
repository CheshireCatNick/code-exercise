def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    arr = RA()
    isPeak = [False] * len(arr)
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
            isPeak[i] = True
    peakCount = 0
    for i in range(1, k - 1):
        if isPeak[i]: peakCount += 1
    best = peakCount
    bestStart = 0
    for i in range(k, n):
        if isPeak[i - 1]:
            peakCount += 1
        if isPeak[i - k + 1]:
            peakCount -= 1
        if peakCount > best:
            best = peakCount
            bestStart = i - k + 1
    print(best + 1, bestStart + 1)


t = int(input())
for i in range(t):
    solve()