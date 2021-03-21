# Generate the Pascal Triangle

def pascalTriangle(n):
    trow = [1]
    y = [0]

    for i in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    
    return n >= 1

n = int(input("n: "))

pascalTriangle(n)