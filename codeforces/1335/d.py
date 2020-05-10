def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    for i in range(9):
        l = input()
        n = ""
        for c in l:
            if c == "1":
                n += "2"
            else:
                n += c
        print(n)

t = int(input())
for i in range(t):
    solve()