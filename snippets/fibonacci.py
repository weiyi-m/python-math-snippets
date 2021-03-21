# Generate the first n Fibonacci numbers

def fibonacci(n):
    if n <= 0:
        return[0]

    sequence = [0, 1]

    while len(sequence) <= n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    
    print(sequence)

n = int(input("n: "))

fibonacci(n)