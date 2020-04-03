def search(arr, val):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if val < arr[mid]:
            r = mid
        elif arr[mid] < val:
            l = mid + 1
        else:
            return mid
    return -1

print(search([1, 2, 3, 4, 5], 1))
print(search([1, 2, 3, 4, 5], 2))
print(search([1, 2, 3, 4, 5], 3))
print(search([1, 2, 3, 4, 5], 4))
print(search([1, 2, 3, 4, 5], 5))
print(search([1, 2, 3, 4, 5], 6))
print(search([3, 3, 3, 3, 3], 3))
print(search([3, 3, 3, 3, 3], 2))