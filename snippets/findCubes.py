# Generate cubes number pattern from 1 to n

def findCubes(n):
    for i in range(1, n + 1):
        cube = i ** 3
        print(cube, end=", ")

n = int(input("n: "))

findCubes(n)