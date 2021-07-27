def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    a = RA()
    b = RA()
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] >= b[i]:
            break
        a[i] = b[i]
    print(sum(a)) 



t = int(input())
for i in range(t):
    solve()