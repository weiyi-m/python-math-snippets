# Generate squares number pattern from 1 to n

def findSquares(n):
    for i in range(1, n + 1):
        square = i ** 2
        print(square, end=", ")

n = int(input("n: "))

findSquares(n)