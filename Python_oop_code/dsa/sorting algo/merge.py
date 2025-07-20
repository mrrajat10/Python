def lrsort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = lrsort(arr[:mid])
    right = lrsort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


arr = [2, 0, 4, 34, 22, 66, 2, 4]
print(lrsort(arr))
