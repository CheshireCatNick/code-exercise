def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    bestEnding = RA()
    for i in range(n - 1):
        a = RA()
        newBestEnding = [
            max(bestEnding[1], bestEnding[2]) + a[0],
            max(bestEnding[0], bestEnding[2]) + a[1],
            max(bestEnding[0], bestEnding[1]) + a[2]
        ]
        bestEnding = newBestEnding
    print(max(bestEnding))


solve()