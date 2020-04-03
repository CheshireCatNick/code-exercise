def isP(s):
    l = 0
    r = len(s) - 1
    while r > l and s[l] == s[r]:
        r -= 1
        l += 1
    return r <= l
def getLongestP(s):
    r = len(s)
    while not isP(s[:r]):
        r -= 1
    return s[:r]
def reverse(s):
    return s[::-1]
    
t = int(input())
for i in range(t):
    s = input()
    l = 0
    r = len(s) - 1
    while r > l and s[l] == s[r]:
        l += 1
        r -= 1
    if r <= l:
        print(s)
        continue
    middle = s[l:r + 1]
    right = getLongestP(middle)
    left = reverse(getLongestP(reverse(middle)))
    final = right if len(right) > len(left) else left
    print(s[:l] + final + s[r + 1:])