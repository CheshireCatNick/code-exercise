def isPal(s):
    l = 0
    r = len(s) - 1
    while r > l and s[l] == s[r]:
        l += 1
        r -= 1
    return r <= l

s = input()
n = len(s)
if (isPal(s) and isPal(s[:int((n - 1) / 2)]) and isPal(s[int((n + 3) / 2) - 1:])):
    print("Yes")
else:
    print("No")