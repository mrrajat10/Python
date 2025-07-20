rows = int(input())
cols = int(input())
for i in range(1, rows+1):
    for j in range(1, cols+1):
        if (i == 1 or j == 1 or i == rows or j == cols):
            print("1", end=" ")

        else:
            print("0", end=" ")
    print()
