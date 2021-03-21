# Find the highest common factor of a and b

def highestCommonFactor1(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a

    for i in range(1, smaller + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i

    print(hcf)

a = int(input("a: "))
b = int(input("b: "))

highestCommonFactor1(a, b)

