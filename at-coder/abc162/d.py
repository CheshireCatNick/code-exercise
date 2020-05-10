n = int(input())
s = input()
pos = {
    "R": [],
    "G": [],
    "B": []
}
for i in range(n):
    pos[s[i]].append(i)
# count of "X" after pos i
count = {
    "R": [0] * n,
    "G": [0] * n,
    "B": [0] * n
}
for i in range(n - 2, -1, -1):
    prevC = s[i + 1]
    for c in "RGB":
        count[c][i] = count[c][i + 1]
    count[prevC][i] += 1
#print(pos)
#print(count)
ans = 0
for i in range(n):
    if s[i] == "R":
        for p in pos["G"]:
            if p > i:
                d = p - i
                ans += count["B"][p]
                if p + d < n and s[p + d] == "B":
                    ans -= 1
        for p in pos["B"]:
            if p > i:
                d = p - i
                ans += count["G"][p]
                if p + d < n and s[p + d] == "G":
                    ans -= 1

    if s[i] == "G":
        for p in pos["R"]:
            if p > i:
                d = p - i
                ans += count["B"][p]
                if p + d < n and s[p + d] == "B":
                    ans -= 1
        for p in pos["B"]:
            if p > i:
                d = p - i
                ans += count["R"][p]
                if p + d < n and s[p + d] == "R":
                    ans -= 1

    if s[i] == "B":
        for p in pos["G"]:
            if p > i:
                d = p - i
                ans += count["R"][p]
                if p + d < n and s[p + d] == "R":
                    ans -= 1
        for p in pos["R"]:
            if p > i:
                d = p - i
                ans += count["G"][p]
                if p + d < n and s[p + d] == "G":
                    ans -= 1
print(ans)

