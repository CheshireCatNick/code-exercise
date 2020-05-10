def RA():
    return list(map(int, input().split()))

def solve():
    a, b, c = RA()
    if b == 0:
        if a > 0:
            print("0" * (a + 1))
            return
        elif c > 0:
            print("1" * (c + 1))
            return
    ans = ""
    for i in range(a + 1):
        ans += "0"
    ans += "1"
    b -= 1
    for i in range(c):
        ans += "1"
    p = 0
    for i in range(b):
        ans += str(p)
        p ^= 1
    print(ans)

t = int(input())
for i in range(t):
    solve()