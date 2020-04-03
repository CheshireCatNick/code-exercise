def RA():
    l = input().split()
    return list(map(lambda x: int(x), l))

n = int(input())
a = RA()
m = {}
for ai in a:
    if not ai in m.keys():
        m[ai] = 1
    else:
        m[ai] += 1
total = 0
for ai in m.keys():
    c = m[ai]
    total += int(c * (c - 1) / 2)
    m[ai] = int((c * (c - 1) - (c - 1) * (c - 2)) / 2)
for ai in a:
    print(total - m[ai])

