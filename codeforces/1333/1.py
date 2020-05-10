def RA():
    l = input().split()
    return [int(s) for s in l]

T = int(input())
for t in range(T):
    [n, m] = RA()
    color = "BW"
    now = 0
    for i in range(n):
        l = []
        for j in range(m):
            l.append(color[now])
            now ^= 1
        if i == n - 1 and not (n % 2 == 1 and m % 2 == 1):
            if n % 2 == 0:
                l[0] = "B"
            else:
                l[1] = "B"
        print("".join(l))
        if m % 2 == 0:
            now ^= 1

            


