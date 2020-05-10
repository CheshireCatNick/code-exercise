def RA():
    l = input().split()
    return [int(s) for s in l]

pos = {}
def l3p(a, b):
    i = 0
    j = 0
    aPos = pos[a]
    bPos = pos[b]
    arr = []
    while i < len(aPos) and j < len(bPos):
        if aPos[i] < bPos[j]:
            arr.append(a)
            i += 1
        else:
            arr.append(b)
            j += 1
    arr += [a] * (len(aPos) - i)
    arr += [b] * (len(bPos) - j)
    #print(arr)
    x = 0
    y = len(bPos)
    l = 0
    r = len(arr) - 1
    best = 1
    while l < r:
        while l < r and not arr[l] == a:
            y -= 1
            l += 1
        while l < r and not arr[r] == a:
            y -= 1
            r -= 1
        if l == r:
            break
        x += 1
        best = max(2 * x + y, best)
        l += 1
        r -= 1
    #print(best)
    return best

def solve():
    global pos
    n = int(input())
    arr = RA()
    for i in range(n):
        num = arr[i]
        if num in pos:
            pos[num].append(i)
        else:
            pos[num] = [i]
    ans = 1
    for a in pos:
        for b in pos:
            if a == b:
                ans = max(ans, len(pos[a]))
            else:
                ans = max(ans, l3p(a, b))
    print(ans)
    pos = {}

t = int(input())
for i in range(t):
    solve()