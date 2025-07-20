arr = [0, 2, 5, 7, 4, 6, 10, 20, -10]
target_sum = 10
n = len(arr)

found = 0
for i in range(0, n):
    for j in range(i+1, n):
        if (arr[i]+arr[j] == target_sum):
            print(f"({arr[i]},{arr[j]})")
            found = 1
if not found:
    print("pairs not found")
