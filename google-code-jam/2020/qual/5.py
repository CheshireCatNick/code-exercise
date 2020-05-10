def RA():
    l = input().split()
    return [int(i) for i in l]

def printM(m):
    for i in range(len(m)):
        print(*m[i])

# try to fill m[i][j]
def latin(n, k, diaSum, m, i, j, avail):
    #printM(m)
    #print(i, j)
    #print(avail)
    if i == n:
        if diaSum == k:
            return True
        else:
            return False
    for num in range(1, n + 1):
        if not avail[num]:
            continue
        ok = True
        for h in range(0, i):
            if m[h][j] == num:
                ok = False
                break
        if not ok:
            continue
        else:
            m[i][j] = num
            if i == j:
                diaSum += num
                if diaSum > k:
                    return False
            if j == n - 1:
                nextAvail = [True] * (n + 1)
                nextAvail[0] = False
                found = latin(n, k, diaSum, m, i + 1, 0, nextAvail)
                if found: return found
            else:
                nextAvail = avail.copy()
                nextAvail[num] = False
                found = latin(n, k, diaSum, m, i, j + 1, nextAvail)
                if found: return found
            if i == j:
                diaSum -= num

t = int(input())
for tc in range(t):
    arr = RA()
    n = arr[0]
    k = arr[1]
    m = []
    for i in range(n):
        m.append([0] * n)
    avail = [True] * (n + 1)
    avail[0] = False
    if (latin(n, k, 0, m, 0, 0, avail)):
        print("Case #{}: POSSIBLE".format(tc + 1))
        printM(m)
    else:
        print("Case #{}: IMPOSSIBLE".format(tc + 1))