def RA():
    l = input().split()
    return [int(s) for s in l]

r = 0
c = 0
s = []
def move(pos, d):
    dirs = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
    np = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
    if np[0] < 0 or np[0] >= r or np[1] < 0 or np[1] >= c:
        return (-1, -1)
    return np

def getNeigh(pos, d):
    while True:
        np = move(pos, d)
        if np == (-1, -1):
            return 0
        if not s[np[0]][np[1]] == 0:
            return s[np[0]][np[1]]
        pos = np

def solve():
    global r, c, s
    [r, c] = RA()
    s = []
    for i in range(r):
        s.append(RA())
    removed = []
    for i in range(r):
        removed.append([False] * c)
    ans = 0
    while True:
        for i in range(r):
            ans += sum(s[i])
        removedCount = 0
        for i in range(r):
            for j in range(c):
                if s[i][j] == 0: continue
                count = 0
                ns = 0
                for d in range(4):
                    n = getNeigh((i, j), d)
                    if not n == 0:
                        count += 1
                        ns += n
                if s[i][j] * count < ns:
                    removed[i][j] = True
                    removedCount += 1
        if removedCount == 0:
            print(ans)
            return
        for i in range(r):
            for j in range(c):
                if removed[i][j]:
                    s[i][j] = 0

t = int(input())
for i in range(t):
    print("Case #{}: ".format(i + 1), end="")
    solve()