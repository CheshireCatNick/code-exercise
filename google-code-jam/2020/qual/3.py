def RA():
    l = input().split()
    return [int(i) for i in l]

t = int(input())
for tc in range(t):
    n = int(input())
    events = []
    for i in range(n):
        arr = RA()
        events.append((arr[0], arr[1], i))
    events.sort()
    cAvail = -1
    jAvail = -1
    assign = ['u'] * n
    fail = False
    for event in events:
        if cAvail <= event[0]:
            assign[event[2]] = 'C'
            cAvail = event[1]
        elif jAvail <= event[0]:
            assign[event[2]] = 'J'
            jAvail = event[1]
        else:
            fail = True
            break
    result = ""
    if fail:
        result = "IMPOSSIBLE"
    else:
        for i in range(n):
            result += assign[i]
    print("Case #{}: {}".format(tc + 1, result))