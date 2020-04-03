t = int(input())
while t > 0:
    s = input()
    prev = -1
    ans = 0
    for i in range(len(s)):
        if s[i] == 'R':
            tmp = i - prev
            ans = max(ans, tmp)
            prev = i
    ans = max(len(s) - prev, ans)
    print(ans)
    t -= 1
