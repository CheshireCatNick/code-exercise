p = [1/2, 2/3, 3/4]
k = 20
ans = 0
succ = p[0] * p[1] * p[2]
for k in range(k + 1):
    res = 0
    for a in range(k + 1):
        for b in range(k + 1):
            if a + b > k:
                continue
            c = k - a - b
            res += pow(1 - p[0], a) * pow(1 - p[1], b) * pow(1 - p[2], c)
    ans += res
print(ans * succ)