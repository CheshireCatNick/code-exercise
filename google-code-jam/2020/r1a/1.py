def RA():
    l = input().split()
    return [int(s) for s in l]

def solve():
    n = int(input())
    s = []
    for i in range(n):
        p = input()
        s.append((p, 0, len(p) - 1))
    prefix = ""
    while True:
        count = {}
        for i in range(n):
            j = s[i][1]
            c = s[i][0][j]
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
            if c != "*":
                s[i] = (s[i][0], s[i][1] + 1, s[i][2])
        if len(count) > 2 or (len(count) == 2 and not "*" in count):
            print("*")
            return
        if "*" in count and count["*"] == n:
            break
        for i in count:
            if i == "*": continue
            prefix += i
    #print(prefix)
    suffix = ""
    while True:
        count = {}
        for i in range(n):
            j = s[i][2]
            c = s[i][0][j]
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
            if c != "*":
                s[i] = (s[i][0], s[i][1], s[i][2] - 1)
        if len(count) > 2 or (len(count) == 2 and not "*" in count):
            print("*")
            return
        if "*" in count and count["*"] == n:
            break
        for i in count:
            if i == "*": continue
            suffix += i
    #print(suffix[::-1])
    middle = ""
    for i in range(n):
        start = s[i][1]
        end = s[i][2] + 1
        middle += s[i][0][start:end].replace("*", "")
    print(prefix + middle + suffix[::-1])

t = int(input())
for i in range(t):
    print("Case #{}: ".format(i + 1), end="")
    solve()