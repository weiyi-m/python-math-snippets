# What are the odd numbers from 1 to n?

def oddNumberRange(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=', ')

n = int(input("n: "))

oddNumberRange(n);