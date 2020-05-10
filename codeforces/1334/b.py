def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    [n, x] = RA()
    arr = RA()
    arr.sort(reverse=True)
    count = 0
    fail = False
    s = 0
    for i in range(n):
        count += 1
        s += arr[i]
        if s < x * count:
            fail = True
            break
    if fail:
        print(count - 1)
    else:
        print(n)

t = int(input())
while t > 0:
    solve()
    t -= 1