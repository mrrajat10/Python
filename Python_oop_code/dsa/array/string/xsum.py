def pair(arr, x):
    n = len(arr)
    seen = set()
    pairs = set()
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == x:
                pair = tuple(sorted((arr[i], arr[j])))
                if pair not in seen:
                    print(f"Pair found: {pair}")
                    seen.add(pair)
                    pairs.add(pair)
    if not pairs:
        print("No pairs found.")
    return pairs  # ✅ return the set


# Test it
arr = [18, 24, 11, 9, 32, 2]
x = 20
result = pair(arr, x)

print("Set of all unique pairs:", result)  # ✅ print outside
