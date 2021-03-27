fibo_cache = {}

def fibo(n):
    if n in fibo_cache:
        return fibo_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibo(n-1)+fibo(n-2)

    fibo_cache[n] = value
    return value

n = int(input("n: "))
print(fibo(n))