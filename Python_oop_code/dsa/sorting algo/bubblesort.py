def bubble(arr, n):
    for i in range(n):
        swapped = 0
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = 1
        if not swapped:
            break
    return arr


arr = [20, 30, 10, 22, 99, 3]
n = len(arr)

print(bubble(arr, n))
