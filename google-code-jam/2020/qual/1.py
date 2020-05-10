def RA():
    l = input().split()
    return list(map(lambda x: int(x), l))

t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(RA())
    rowRep = 0
    colRep = 0
    diagSum = 0
    for j in range(n):
        for k in range(n):
            if j == k:
                diagSum += arr[j][k]
    for j in range(n):
        exist = {}
        for k in range(n):
            if arr[j][k] in exist:
                rowRep += 1
                break
            exist[arr[j][k]] = True
    for j in range(n):
        exist = {}
        for k in range(n):
            if arr[k][j] in exist:
                colRep += 1
                break
            exist[arr[k][j]] = True
    print("Case #{}: {} {} {}".format(i + 1, diagSum, rowRep, colRep))   
            


