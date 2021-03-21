# Make a list containing all factors of n.

def findFactorsList(n):
    nlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            nlist.append(i)
    print(nlist)

n = int(input("n: "))

findFactorsList(n)

