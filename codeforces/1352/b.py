def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    if k == 1:
        print("YES")
        print(n)
        return
    if n < k:
        print("NO")
        return
    if n % 2 == 0:
        if k % 2 == 1:
            if n - 2 * (k - 1) < 1:
                print("NO")
            else:
                print("YES")
                print(*([2] * (k - 1) + [n - 2 * (k - 1)]))
        else:
            print("YES")
            print(*([1] * (k - 1) + [n - (k - 1)]))
    else:
        if k % 2 == 0:
            print("NO")
        else:
            print("YES")
            print(*([1] * (k - 1) + [n - (k - 1)]))

        

t = int(input())
for i in range(t):
    solve()