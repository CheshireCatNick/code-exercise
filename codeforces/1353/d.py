import heapq

def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    q = [(-n, 0, n - 1)]
    heapq.heapify(q)
    ans = [0] * n
    for i in range(1, n + 1):
        length, l, r = heapq.heappop(q)
        pos = (l + r) // 2
        ans[pos] = i
        if pos - 1 >= l: 
            heapq.heappush(q, (-(pos - l),l, pos - 1))
        if pos + 1 <= r: 
            heapq.heappush(q, (-(r - pos), pos + 1, r))
    print(*ans)

t = int(input())
for i in range(t):
    solve()