# What are the even numbers from 1 to n?

def evenNumberRange(n):
    for i in range(1, n + 1):
        if (i % 2 == 0):
            print(i, end=', ')

n = int(input("n: "))

evenNumberRange(n)

