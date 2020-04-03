def RA():
    l = input().split()
    return list(map(lambda x: int(x), l))
    
a = RA()
n = a[0]
m = a[1]
print(int(m * (m - 1) / 2 + n * (n - 1) / 2))