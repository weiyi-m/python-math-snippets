# Is n a composite number?
# A composite number is an integer that is not a prime number.

def isComposite(n):
    n_factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            n_factors += 1
    
    if n_factors > 2:
        print("True")
    else:
        print("False")

n = int(input("n: "))

isComposite(n)
