def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for item in arr[1:]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    return quick(left) + [pivot] + quick(right)


arr = [23, 34, 55, 3, 4, 52, 2, -3]
re = quick(arr)
print(re)
