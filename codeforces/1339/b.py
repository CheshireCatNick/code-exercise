def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    arr = RA()
    arr.sort()
    left = arr[:n // 2]
    right = arr[n // 2:]
    ans = []
    ri = 0
    li = len(left) - 1
    for i in range(n):
        if i % 2 == 0:
            ans.append(right[ri])
            ri += 1
        else:
            ans.append(left[li])
            li -= 1
    print(*ans)

t = int(input())
for i in range(t):
    solve()