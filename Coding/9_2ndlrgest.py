a, b, c = map(int, input("Enter 3 no:").split())
if a >= b and a >= c:
    if (b >= c):
        print(b)
    else:
        print(c)
elif b >= c and b >= a:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if (a > b):
        print(a)
    else:
        print(b)
