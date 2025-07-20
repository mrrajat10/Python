def selection(arr, n):
    for i in range(n-1):
        sm = i
        for j in range(i+1, n):
            if (arr[sm] > arr[j]):
                sm = j
        arr[i], arr[sm] = arr[sm], arr[i]
    return arr


arr = [21, 2, 4, 23, 5, 45, 21]
n = len(arr)
print(selection(arr, n))
