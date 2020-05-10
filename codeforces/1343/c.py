def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    a = RA()
    isPositive = a[0] > 0
    m = a[0]
    result = 0
    for num in a:
        if isPositive:
            if num > 0:
                m = max(m, num)
            else:
                result += m
                m = num
                isPositive = False
        else:
            if num < 0:
                m = max(m, num)
            else:
                result += m
                m = num
                isPositive = True
    print(result + m)
        



t = int(input())
for i in range(t):
    solve()