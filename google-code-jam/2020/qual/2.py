def RA():
    l = input()
    return [int(i) for i in l]

t = int(input())
for tc in range(t):
    arr = RA()
    arr = [0] + arr + [0]
    newArr = []
    for i in range(1, len(arr)):
        newArr.append(arr[i] - arr[i - 1])
    k = 1
    result = ''
    for i in range(len(newArr) - 1):
        n = newArr[i]
        if (n > 0):
            for j in range(n):
                result += '('
        elif (n < 0):
            for j in range(abs(n)):
                result += ')'
        result += str(arr[k])
        k += 1
    n = newArr[-1]
    for j in range(abs(n)):
        result += ')'
    print("Case #{}: {}".format(tc + 1, result))
