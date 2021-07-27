def RA():
    return list(map(int, input().split()))

def solve():
    n, k = RA()
    s = input()
    pref = [0, 1 if s[0] == "1" else 0]
    for i in range(1, len(s)):
        pref.append(pref[i] + 1 if s[i] == "1" else pref[i])
    #print(pref)
    ans = []
    for i in range(k):
        print("i =", i)
        now = i
        move = 0
        prev = -1
        while now < n:
            if s[now] == "0":
                move += 1
            if k > 1:
                print(now, prev)
                move += pref[now] - pref[prev + 1]
            prev = now
            now += k
            print(move)
        move += pref[-1] - pref[prev + 1]

        ans.append(move)
    ans.sort()
    print(ans[0])

t = int(input())
for i in range(t):
    solve()