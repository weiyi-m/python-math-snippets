# What are the factors of n?
# A factor is a integer which when multiplied with another integer outputs n.
# n can be divided by a factor of n in order to output an integer with no remainders.

def findFactors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=", ")

n = int(input("n: "))

findFactors(n)
