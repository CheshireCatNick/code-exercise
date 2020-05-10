def RA():
    l = input().split()
    return [int(s) for s in l]

def dfs(node, parent, depth):
    totalChild = 0
    for c in child[node]:
        if c == parent:
            continue
        totalChild += dfs(c, node, depth + 1)
    scores[node] = depth - totalChild
    return totalChild + 1

[n, k] = RA()
child = [[] for i in range(n)]
for i in range(n - 1):
    [u, v] = RA()
    child[u - 1].append(v - 1)
    child[v - 1].append(u - 1)
scores = [0] * n
dfs(0, None, 0)
print(sum(sorted(scores, reverse=True)[:k]))
