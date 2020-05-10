def RA():
    l = input().split()
    return [int(s) for s in l]
isVisited = {}
pascals = []
def create(n):
    for i in range(n):
        if i == 0:
            pascals.append([0])
            pascals.append([0, 1, 0])
            continue
        new = []
        for j in range(1, len(pascals[i])):
            new.append(pascals[i][j] + pascals[i][j - 1])
        print(i, new)
        pascals.append([0] + new + [0])

def getPath(pos, n):
    if n < pascals[pos[0]][pos[1]]:
        return []
    if n == pascals[pos[0]][pos[1]]:
        return [pos]
    nes = [
        (pos[0] - 1, pos[1] - 1),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
        (pos[0] + 1, pos[1]),
        (pos[0] + 1, pos[1] + 1),
    ]
    isVisited[pos] = True
    for ne in nes:
        if ne[0] < 1 or ne[1] < 1:
            continue
        path = getPath(ne, n - pascals[pos[0]][pos[1]])
        if not len(path) == 0:
            return [pos] + path

def solve():
    n = int(input())
    global isVisited
    isVisited = {}
    create(n)
    print(pascals)
    path = getPath((1, 1), n)
    for p in path:
        print(p[0], p[1])

t = int(input())
for i in range(t):
    print("Case #{}: ".format(i + 1))
    solve()