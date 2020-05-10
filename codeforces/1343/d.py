def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n, k = RA()
    arr = RA()
    scores = [[0, 0, 0] for i in range(2 * k + 1)]
    for i in range(n // 2):
        a = arr[i]
        b = arr[n - i - 1]
        mini = min(a, b) + 1
        maxi = a + b + k - min(a, b)
        scores[mini][0] += 1
        scores[a + b][1] += 1
        scores[maxi][2] += 1
    needChange = n
    best = needChange
    for i in range(2, 2 * k + 1):
        needChange -= scores[i][0]
        best = min(best, needChange - scores[i][1])
        needChange += scores[i][2]
    print(best)
        
t = int(input())
for i in range(t):
    solve()