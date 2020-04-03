def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    i = 0
    j = 0
    result = []
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif right[j] < left[i]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

arr = [3, 2, 4, 1, 5]
print(mergeSort(arr))