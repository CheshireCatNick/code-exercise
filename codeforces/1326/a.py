t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(-1)
        continue
    print('3' * (n - 1) + '4')