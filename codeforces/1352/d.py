def RA():
    return list(map(int, input().split()))

def solve():
    n = int(input())
    arr = RA()
    l = 0
    r = n
    
    aliceEat = arr[0]
    a = arr[0]
    b = 0
    count = 1
    while l != r - 1:
        # bob eat
        bobEat = 0
        while l != r - 1 and bobEat <= aliceEat:
            r -= 1
            bobEat += arr[r]
        b += bobEat
        count += 1
        if l == r - 1:
            break
        # alice eat
        aliceEat = 0
        while l != r - 1 and aliceEat <= bobEat:
            l += 1
            aliceEat += arr[l]
        a += aliceEat
        count += 1
    print(count, a, b)

t = int(input())
for i in range(t):
    solve()