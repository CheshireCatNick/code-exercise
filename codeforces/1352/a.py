def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    result = []
    m = 1
    while n > 0:
        if n % 10 != 0:
            result.append(n % 10 * m)
        n //= 10
        m *= 10
    print(len(result))
    print(*result)    

t = int(input())
for i in range(t):
    solve()