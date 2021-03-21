# Generate multiples of n from a to b

def findMultipleRange(n, a, b):
    for i in range(a, b + 1):
        if i % n == 0:
            print(i, end=", ")

n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))

findMultipleRange(n, a, b)