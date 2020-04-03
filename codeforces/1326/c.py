l1 = input().split(' ')
n = int(l1[0])
k = int(l1[1])
p = input().split(' ')
p = [int(i) for i in p]

pv = k * (2 * n - k + 1) / 2

ans = 1
prev = -1
small = n - k + 1
MOD = 998244353
for i in range(len(p)):
    if p[i] >= small:
        if prev == -1:
            prev = i
            continue
        ans *= (i - prev)
        ans %= MOD
        prev = i

print(int(pv), ans)


