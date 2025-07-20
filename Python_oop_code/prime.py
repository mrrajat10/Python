def prime(n):
    if n <= 1:
        return "Invalid Syntax"

    for i in range(2, n):
        if n % i == 0:
            print("It is a prime no")
    return "It is a prime"


p = prime(11)
print(p)
