def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    [n, a, b] = RA()
    s = ""
    for i in range(26):
        s += chr(ord('a') + i)
    s = s[:b]
    result = ""
    for i in range(n):
        result += s[i % b]
    print(result)

t = int(input())
for i in range(t):
    solve()